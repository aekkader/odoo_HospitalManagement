# -*- coding: utf-8 -*-
# from odoo import http


# class A14Custom(http.Controller):
#     @http.route('/a14_custom/a14_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/a14_custom/a14_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('a14_custom.listing', {
#             'root': '/a14_custom/a14_custom',
#             'objects': http.request.env['a14_custom.a14_custom'].search([]),
#         })

#     @http.route('/a14_custom/a14_custom/objects/<model("a14_custom.a14_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('a14_custom.object', {
#             'object': obj
#         })
