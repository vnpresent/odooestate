from odoo import api,fields,models

class School(models.Model):
    _name = "school.information"
    _description = "Quản Lý Trường Học"
    name = fields.Char(string="Tên Trường Học")
    address = fields.Char(string="Địa Chỉ")
    type = fields.Selection([('public','Công Lập'),('private','Dân Lập')],default='public',string="Loại Trường")
    date = fields.Date(string="Ngày Thành Lập")
    class_list  = fields.One2many("class.information","school_id","Danh Sách Lớp")