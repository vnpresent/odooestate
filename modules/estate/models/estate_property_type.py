from odoo import models,fields
class Type(models.Model):
    _name = "estate.property.type"
    _description = "this is type "
    _order = "name desc"
    estate_id = fields.Many2one("estate.property")
    name = fields.Char(string="Tên",required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    note = fields.Char(string="Ghi chú",required=True)
