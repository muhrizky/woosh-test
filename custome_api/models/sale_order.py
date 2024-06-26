from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create_sale_order(self, order_data):
        # Method to create a sale order
        sale_order = self.create({
            'partner_id': order_data['partner_id'],
            'note': 'From API Create Order',
            'order_line': [(0, 0, {
                'product_id': line['product_id'],
                'product_uom_qty': line['quantity'],
                'price_unit': line['price_unit'],
            }) for line in order_data['order_lines']]
        })
        sale_order.action_confirm()
        invoice = sale_order._create_invoices()
        invoice.action_post()
        payment_register_vals = {
            'amount': invoice.amount_total,
            'payment_date': fields.Date.context_today(self),
            'communication': invoice.name,
            'journal_id': self.env['account.journal'].search([('type', '=', 'bank')], limit=1).id,
            'payment_type': 'inbound',
            'partner_type': 'customer',
            'partner_id': sale_order.partner_id.id,
            'payment_method_id': self.env.ref('account.account_payment_method_manual_in').id,
        }
        payment_register = self.env['account.payment.register'].with_context(
            active_model='account.move',
            active_ids=invoice.ids,
        ).create(payment_register_vals)
        payments = payment_register._create_payments()
        return sale_order, invoice, payments