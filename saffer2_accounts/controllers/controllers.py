# -*- coding: utf-8 -*-
# from odoo import http


# class Saffer2Accounts(http.Controller):
#     @http.route('/saffer2_accounts/saffer2_accounts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saffer2_accounts/saffer2_accounts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saffer2_accounts.listing', {
#             'root': '/saffer2_accounts/saffer2_accounts',
#             'objects': http.request.env['saffer2_accounts.saffer2_accounts'].search([]),
#         })

#     @http.route('/saffer2_accounts/saffer2_accounts/objects/<model("saffer2_accounts.saffer2_accounts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saffer2_accounts.object', {
#             'object': obj
#         })
