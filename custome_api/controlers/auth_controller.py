import functools
import json
import jwt
import logging
from odoo import http
from odoo.http import request
import datetime

_logger = logging.getLogger(__name__)

JWT_SECRET = 'tes_odoo_engineer_efishery'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 3600

active_tokens = {}


def invalid_response(error_code, error_message, status_code):
    return http.Response(
        json.dumps({'error': error_code, 'message': error_message}),
        headers={'Content-Type': 'application/json'},
        status=status_code
    )


def validate_token(func):
    """Decorator to validate JWT token in the request header."""

    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
        """Wrap the function to validate the token."""
        access_token = request.httprequest.headers.get("token")
        if not access_token:
            return invalid_response("access_token_not_found", "Missing access token in request header", 401)
        try:
            decoded_token = jwt.decode(access_token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            email = decoded_token.get('email')
        except jwt.ExpiredSignatureError:
            return invalid_response("access_token_expired", "Token has expired", 401)
        except jwt.InvalidTokenError:
            return invalid_response("access_token_invalid", "Invalid token", 401)

        user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
        if not user:
            return invalid_response("user_not_found", "User not found", 401)

        request.session.uid = user.id
        request.uid = user.id

        return func(self, *args, **kwargs)

    return wrap


class AuthJWTController(http.Controller):
    @http.route('/authenticate/login', type='json', auth='none', methods=['POST'], csrf=False)
    def login(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return json.dumps({'error': 'Email and password required'})

        user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)

        if not user or not request.env['res.users'].sudo().authenticate(request.db, email, password,
                                                                        {'interactive': False}):
            return json.dumps({'error': 'Invalid email or password'})
        if email in active_tokens:
            return json.dumps({'error': 'User already logged in on another device'})

        payload = {
            'email': user.login,
            'role': user.has_group('base.group_user') and 'user' or 'admin',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
        active_tokens[email] = token

        return json.dumps({'token': token})

    @http.route('/authenticate/logout', type='json', auth='none', methods=['POST'], csrf=False)
    def logout(self, **kwargs):
        token = kwargs.get('token')

        if not token:
            return json.dumps({'error': 'Token required'})
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            email = decoded_token.get('email')
        except jwt.ExpiredSignatureError:
            return json.dumps({'error': 'Expired token'})
        except jwt.InvalidTokenError:
            return json.dumps({'error': 'Invalid token'})
        if email not in active_tokens or active_tokens[email] != token:
            return json.dumps({'error': 'Invalid token'})
        del active_tokens[email]

        return json.dumps({'message': 'Logout successful'})
