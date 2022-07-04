from odoo import models,fields,api
from odoo.exceptions import ValidationError
class Offer(models.Model):
    _name = "estate.property.offer"
    _description = "this is offer "
    _order = "price desc"
    price = fields.Float(string="Giá")
    partner_id = fields.Many2one("res.partner",string="Partner",required=True)
    property_id = fields.Many2one("estate.property",string="Estate",required=True)
    status = fields.Selection([('Accepted','Chấp Nhận'),('Refused','Từ chối')],string="Trạng thái",copy=False)
    thisstate = fields.Selection(related='property_id.state')

    # property_type_id = fields.Integer(related="zy")

    _sql_constraints = [
        ('check_price', 'CHECK(price>=0)','Giá offer phải dương'),
    ]

    def action_accepted(self):
        for record in self:
            if record.property_id.state != "Sold" and record.status != "Refused":
                record.status = "Accepted"
                record.property_id.state = "Offer Accepted"
                record.property_id.selling_price = record.price
                record.property_id.partner_id = record.partner_id
                return True
            else:
                return False
    
    def action_refused(self):
        for record in self:
            if record.status != "Sold":
                record.status = "Refused"
                record.property_id.state = "New"
        return True
    
    @api.model
    def create(self, values):
        # print(self.env['estate.property'].browse(values['property_id']).expected_price)
        # print(self.env['estate.property'].browse(values['property_id']).best_price)
        if values['price'] > self.env['estate.property'].browse(values['property_id']).best_price:
            return super(Offer, self).create(values)
        else:
            raise ValidationError("Giá đặt không đc nhỏ hơn giá tốt nhất")
