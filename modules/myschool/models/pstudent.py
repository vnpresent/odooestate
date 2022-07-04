from odoo import api,fields,models

class Student(models.Model):
    _name = "student.information"
    _description = "Quản Lý Học Sinh"
    name = fields.Char(string="Tên Học Sinh")
    address = fields.Char(string="Địa Chỉ")
    date = fields.Date(string="Ngày Sinh")
    class_id = fields.Many2one("class.information",string="Lớp")