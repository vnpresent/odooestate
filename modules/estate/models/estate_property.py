from datetime import timedelta
from odoo import api,models,fields
from odoo.exceptions import ValidationError


class Estate(models.Model):
    _name = "estate.property"
    _description = "this is estate "
    _order = "id desc"
    name = fields.Char(string="Tên",required=True)
    postcode = fields.Char(string="Mã Vùng")
    date_availability = fields.Date(string="Ngày bắt đầu",default=fields.datetime.today()+timedelta(days=90))
    expected_price = fields.Float(string="Giá dự kiến",required=True,copy=False)
    selling_price = fields.Float(string="Giá bán",readonly=True,copy=False) 
    bedrooms = fields.Integer(string="Phòng ngủ",default=2)
    living_area = fields.Integer(string="Diện tích ở")
    facades = fields.Integer(string="Mặt tiền")
    garage = fields.Boolean(string="Gara để xe")
    garden = fields.Boolean(string="Vườn")
    garden_area = fields.Integer(string="Diện tích vườn")
    garden_orientation = fields.Selection([('North','Bắc'),('South','Nam'),('East','Đông'),('West','Tây')],string="Hướng vườn")
    active = fields.Boolean(default=True)
    state = fields.Selection([('New','New'),('Offer Received','Received'),('Offer Accepted','Offer Accepted'),('Sold','Sold'),('Canceled','Canceled')],default='New',string="Trạng thái")

    # property_type_id = fields.One2many("estate.property.type","estate_id")
    salesperson = fields.Many2one('res.users', string='Người bán', index=True, tracking=True, default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string='Người mua',copy=False)
    tag_ids = fields.Many2many("estate.property.tag",string="List tag")
    offer_ids = fields.One2many('estate.property.offer','property_id')


    total_area = fields.Integer(string="Diện tích tổng",compute="compute_total_area",readonly=True)
    best_price = fields.Float(string="Giá tốt nhất",compute="compute_best_price",default=0)
    validity = fields.Integer(string="Ngày hợp lệ",default=7)
    date_deadline = fields.Date(string="Ngày deadline",compute="compute_date_deadline")


    property_ids = fields.One2many("estate.property.type","estate_id")

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)',
        'Giá dự kiến phải dương'),
    ]

    @api.depends('living_area','garden_area')
    def compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    @api.depends('offer_ids.price')
    def compute_best_price(self):
        for record in self:
            if len(record.offer_ids) >0:
                record.best_price = max(record.mapped('offer_ids.price'))
            else:
                record.best_price = 0

    @api.depends('validity','create_date')
    def compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + timedelta(days=record.validity)
    
    @api.onchange('offer_ids')
    def onchange_offer_ids(self):
        for record in self:
            if len(record.offer_ids)>0:
                record.state = "Offer Received"
    
    @api.onchange("garden")
    def onchange_garden(self):
        # print(self.garden)
        if self.garden == True:
            self.garden_area=10
            self.garden_orientation = 'North'
        else:
            self.garden_area = None
            self.garden_orientation = None
    

    def action_cancel(self):
        for record in self:
            if record.state != "Sold":
                record.state = "Canceled"
        return True
    
    def action_sold(self):
        for record in self:
            if record.state != "Canceled":
                record.state = "Sold"
        return True

    @api.constrains('selling_price')
    def _check_description(self):
        for record in self:
            if record.selling_price / (record.expected_price*1.0)<0.9:
                raise ValidationError("Giá bán không được thấp hơn 90% giá dự kiến")
    

    @api.ondelete(at_uninstall=False)
    def _unlink_if_(self):
        for record in self:
            if record.state!="New" and record.state!="Canceled":
                raise ValidationError("Không thể xóa:"+record.name)

