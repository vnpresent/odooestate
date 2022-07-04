from odoo import http
from odoo.http import request
import json

class SchoolController(http.Controller):

    @http.route('/school/<string:id>/',auth="public",type="http", website = True)
    def schoolid(self,id):
        list = http.request.env['school.information'].sudo().search([('id','=',id)])
        data = []
        for school in list:
            cls = []
            for cl in school.class_list:
                value = {
                    'id':cl.id,
                    'name':cl.name
                }
                cls.append(value)
            value = {
                'name':school.name,
                'address':school.address,
                'type':school.type,
                'date':str(school.date),
                'class_list':cls
            }
            data.append(value)
        res = {'code':200,'result':data}
        return json.dumps(res)
    @http.route('/school',auth="public",type="http", website = True)
    def school(self):
        list = http.request.env['school.information'].sudo().search([])
        data = []
        for school in list:
            cls = []
            for cl in school.class_list:
                cls.append(cl.id)
            value = {
                'name':school.name,
                'address':school.address,
                'type':school.type,
                'date':str(school.date),
                'class_list':cls
            }
            data.append(value)
        res = {'code':200,'result':data}
        return json.dumps(res)