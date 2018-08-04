# -*- coding: utf-8 -*-
from odoo import http

# class OpenA(http.Controller):
#     @http.route('/open_a/open_a/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_a/open_a/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_a.listing', {
#             'root': '/open_a/open_a',
#             'objects': http.request.env['open_a.open_a'].search([]),
#         })

#     @http.route('/open_a/open_a/objects/<model("open_a.open_a"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_a.object', {
#             'object': obj
#         })