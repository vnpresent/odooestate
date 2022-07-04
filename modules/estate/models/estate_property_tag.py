from odoo import models,fields
class Tag(models.Model):
    _name = "estate.property.tag"
    _description = "this is tag "
    _order = "name desc"
    name = fields.Char(string="Tên",required=True)
    color = fields.Integer()

    _sql_constraints = [
        ('check_name', 'unique(name)',
         'Tên tag phải là duy nhất'),
    ]