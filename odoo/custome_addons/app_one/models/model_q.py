from odoo import models, fields

class Modelq(models.Model):
    _name = 'model.q'
    _description = 'Model Q'
    
    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)