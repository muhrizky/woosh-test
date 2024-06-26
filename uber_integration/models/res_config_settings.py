from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    uber_base_url = fields.Char(string="Uber Base URL")
    uber_client_id = fields.Char(string="Uber Client ID")
    uber_client_secret = fields.Char(string="Uber Client Secret")
    uber_api_auth = fields.Char(string="Uber Auth API")
    uber_api_order = fields.Char(string="Uber Order API")
    uber_access_token = fields.Char(string="Uber Access Token", readonly=True)
    uber_token_expiry = fields.Datetime(string="Token Expiry", readonly=True)

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('uber.base_url', self.uber_base_url)
        self.env['ir.config_parameter'].sudo().set_param('uber.client_id', self.uber_client_id)
        self.env['ir.config_parameter'].sudo().set_param('uber.client_secret', self.uber_client_secret)
        self.env['ir.config_parameter'].sudo().set_param('uber.access_token', self.uber_access_token)
        self.env['ir.config_parameter'].sudo().set_param('uber.token_expiry', self.uber_token_expiry)
        self.env['ir.config_parameter'].sudo().set_param('uber.api_auth', self.uber_api_auth)
        self.env['ir.config_parameter'].sudo().set_param('uber.api_order', self.uber_api_order)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        config = self.env['ir.config_parameter'].sudo()
        res.update(
            uber_base_url=config.get_param('uber.base_url', default=''),
            uber_client_id=config.get_param('uber.client_id', default=''),
            uber_client_secret=config.get_param('uber.client_secret', default=''),
            uber_access_token=config.get_param('uber.access_token', default=''),
            uber_token_expiry=config.get_param('uber.token_expiry', default=False),
            uber_api_auth=config.get_param('uber.api_auth', default=False),
            uber_api_order=config.get_param('uber.api_order', default=False),
        )
        return res
