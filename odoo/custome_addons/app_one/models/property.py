from odoo import models, fields, api



from odoo.exceptions import ValidationError







class Property(models.Model):



    _name = 'property'



    _description = 'Property'



    _table = 'property'



    



    name = fields.Char()



    description = fields.Text()



    

   

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



    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')



    # SQL Constraint - الاسم الصحيح هو _sql_constraints (بـ t وليس n)

    # _sql_constraints = [ 

    #     ('unique_postcode', 'unique (postcode)', 'Postcode must be unique')

    # ]

   

   



    _name_category_uniq = models.Constraint(
        'unique (name, description)',
        'Tag name already exists in this category!',
    )



    @api.constrains('bedrooms')



    def _check_bedrooms(self):



        for record in self:



            if record.bedrooms == 0:



                raise ValidationError("Bedrooms cannot be zero.")

    # @api.model_create_multi
    # def create(self, vals_list):
    #    res= super(Property, self).create(vals_list)
    #    print("Property created:", res)
    #    return res            
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, **kwargs):
    #     result = super()._search(
    #         domain,
    #         offset=offset,
    #         limit=limit,
    #         order=order,
    #         **kwargs
    #     )
    #     print("Property searched:", self)
    #     return result
    # def write(self, vals):
    #     print("Property written:", self)
    #     return super().write(vals)
    # def unlink(self):
    #     print("deleted method called", self)
    #     return super().unlink()
