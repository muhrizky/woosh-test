from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    is_quality_checked = fields.Boolean(string="Complete Quality Checked", default=False)
    state = fields.Selection(selection_add=[('quality_check', 'Quality Check')])

    def action_quality_check(self):
        self.ensure_one()
        if not self.env.user.has_group('inventory_quality_check.group_stock_quality_manager'):
            raise UserError("Only Stock Managers can perform a quality check.")
        self.write({'state': 'quality_check'})
        self.message_post(body="Inventory moved to Quality Check stage.")

    def button_validate(self):
        if self.state == 'quality_check' and not self.is_quality_checked:
            raise UserError("You must complete the quality check before marking this as done.")
        return super(StockPicking, self).button_validate()

    @api.depends('state')
    def _compute_show_validate(self):
        for picking in self:
            if not (picking.immediate_transfer) and picking.state == 'draft':
                picking.show_validate = False
            elif picking.state == 'assigned' and not self.env.user.has_group(
                    'inventory_quality_check.group_stock_quality_manager'):
                picking.show_validate = True
            elif picking.state not in ('draft', 'waiting', 'confirmed', 'quality_check'):
                picking.show_validate = False
            else:
                picking.show_validate = True
