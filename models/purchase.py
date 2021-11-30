from odoo import fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    notes = fields.Html(string='Terms and conditions')
