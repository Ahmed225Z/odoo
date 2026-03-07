from odoo import models, fields
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _property_id = fields.Many2one('property', string='Property')
   
  
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        # Your custom logic here
        print("Sale order confirmed!")
        print("Property ID:", self._property_id)