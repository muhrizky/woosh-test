import requests
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.http import request, Response


class UberAPI(models.Model):
    _name = 'uber.api'
    _description = 'Uber API Integration'

    @api.model
    def get_access_token(self):
        config = self.env['ir.config_parameter'].sudo()
        base_url = "https://auth.uber.com"
        client_id = config.get_param('uber.client_id')
        client_secret = config.get_param('uber.client_secret')
        token_expiry = config.get_param('uber.token_expiry')
        access_token = config.get_param('uber.access_token')
        path_auth = config.get_param('uber.api_auth')

        if not client_id or not client_secret:
            raise UserError('Client ID and Client Secret must be set in the configuration.')
        if not base_url:
            raise UserError('Base URL must be set in the configuration.')
        if not path_auth:
            raise UserError('Path Auth must be set in the configuration.')

        if not access_token or fields.Datetime.now() > fields.Datetime.from_string(token_expiry):
            url = f"{base_url}{path_auth}"
            payload = {
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': 'client_credentials',
                'scope': 'eats.order'
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            response = requests.post(url, data=payload, headers=headers)
            if response.status_code == 200:
                token_info = response.json()
                config.set_param('uber.access_token', token_info['access_token'])
                config.set_param('uber.token_expiry', fields.Datetime.to_string(
                    fields.Datetime.now() + timedelta(seconds=token_info['expires_in'])))
                access_token = token_info['access_token']
            else:
                raise UserError('Failed to obtain access token: {}'.format(response.text))
        return access_token

    @api.model
    def get_orders(self):
        access_token = self.get_access_token()
        path_order = self.env['ir.config_parameter'].sudo().get_param('uber.api_order')
        base_url = path_order.sudo().get_param('uber.base_url')

        url = "{base_url}{path_order}".format(base_url=base_url, path_order=path_order)
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            order_details = response.json()
            request.env['uber.eats.order'].sudo().create_or_update_order(order_details)
        else:
            raise UserError('Failed to retrieve orders: {}'.format(response.text))
