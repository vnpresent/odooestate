from odoo import http
from odoo.http import request
import json

class ClassController(http.Controller):

    @http.route('/class/<string:id>/',auth="public",type="http", website = True)
    def classid(self,id):
        list = http.request.env['class.information'].sudo().search([('id','=',id)])
        data = []
        for clas in list:
            cls = []
            for cl in clas.student_list:
                value = {
                    'id':cl.id,
                    'name':cl.name
                }
                cls.append(value)
            value = {
                'name':clas.name,
                'grade':clas.grade,
                'school_id':{'id':clas.school_id.id,'name':clas.school_id.name},
                'student_list':cls
            }
            data.append(value)
        res = {'code':200,'result':data}
        return json.dumps(res)
    @http.route('/class',auth="public",type="http", website = True)
    def clas(self):
        list = http.request.env['class.information'].sudo().search([])
        data = []
        for clas in list:
            cls = []
            for cl in clas.student_list:
                value = {
                    'id':cl.id,
                    'name':cl.name
                }
                cls.append(value)
            value = {
                'name':clas.name,
                'grade':clas.grade,
                'school_id':{'id':clas.school_id.id,'name':clas.school_id.name},
                'student_list':cls
            }
            data.append(value)
        res = {'code':200,'result':data}
        return json.dumps(res)
    

    @http.route('/class/add',auth="public",type="http", website = True)
    def classadd(self):
        list = http.request.env['class.information'].sudo().search([])
        data = []
        for clas in list:
            cls = []
            for cl in clas.student_list:
                value = {
                    'id':cl.id,
                    'name':cl.name
                }
                cls.append(value)
            value = {
                'name':clas.name,
                'grade':clas.grade,
                'school_id':{'id':clas.school_id.id,'name':clas.school_id.name},
                'student_list':cls
            }
            data.append(value)
        res = {'code':200,'result':data}
        return json.dumps(res)



