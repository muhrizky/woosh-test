from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'account.move'

    @api.model
    def _get_invoice_in_payment_state(self):
        # OVERRIDE to enable the 'in_payment' state on invoices.
        return 'in_payment'
