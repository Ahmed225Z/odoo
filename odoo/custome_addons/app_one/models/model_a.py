from odoo import models, fields


class ModelA(models.Model):
    _name = 'model.a'
    _description = 'Model A'
    # ahmed = fields.Char(required=True)
    name = fields.Char(string='Name', required=True)
    # description = fields.Text(string='Description')
   
    # _sql_constraints = [

    #     ('model_a_unique_ahmed', 'unique (ahmed)', 'Name must be unique')

    # ]
    _name_uniq_ahmed = models.Constraint(
        'unique (name)',
        'Tag name already exists!',
    )