from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    
    name = fields.Char(required=True, default='name', size=5)
    description = fields.Text(required=True)
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float(digits=(0, 5))
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], default='north')
    
    # SQL Constraints - موحدة داخل الكلاس
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'Name must be unique.')
    ]
    
    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for record in self:
            if record.bedrooms == 0:
                raise ValidationError("Bedrooms cannot be zero.")