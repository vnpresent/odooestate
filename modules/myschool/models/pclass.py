from odoo import api,fields,models

class Class(models.Model):
    _name = "class.information"
    _description = "Quản Lý Lớp Học"
    name = fields.Char(string="Tên Lớp Học")
    grade = fields.Char(string="Khối")
    school_id = fields.Many2one("school.information",string="Trường")
    student_list = fields.One2many("student.information","class_id","Danh Sách Học Sinh")