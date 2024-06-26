from odoo import http
from odoo.http import request, Response
from odoo.addons.custome_api.controlers.auth_controller import validate_token
import json


class CustomApiController(http.Controller):
    @validate_token
    @http.route('/api/customers', type='http', auth='public', methods=['GET'], csrf=False)
    def get_customers(self):
        try:
            customers = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
            customer_list = []
            for customer in customers:
                customer_list.append({
                    'id': customer.id,
                    'name': customer.name,
                    'email': customer.email,
                    'phone': customer.phone
                })
            return json.dumps({'customer_list': customer_list})
        except Exception as e:
            return json.dumps({'error': str(e)})

    @validate_token
    @http.route('/api/products', type='http', auth='public', methods=['GET'], csrf=False)
    def get_products(self):
        try:
            products = request.env['product.product'].sudo().search([])
            product_list = []
            for product in products:
                product_list.append({
                    'id': product.id,
                    'name': product.name,
                    'list_price': product.list_price,
                    'qty_available': product.qty_available
                })
            return json.dumps({'product_list': product_list})
        except Exception as e:
            return json.dumps({'error': str(e)})

    @validate_token
    @http.route('/api/sales_orders', type='json', auth='public', methods=['POST'], csrf=False)
    def create_order(self, **kwargs):
        order_data = request.jsonrequest
        try:
            sale_order, invoice, payment = request.env['sale.order'].sudo().create_sale_order(order_data)
            return {
                'sale_order_id': sale_order.id,
                'invoice_id': invoice.id,
                'payment_id': payment.id,
            }
        except Exception as e:
            return json.dumps({'error': e.name})
