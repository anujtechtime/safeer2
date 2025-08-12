# -*- coding: utf-8 -*-
# from odoo import http


# class SafeerReportInvoice(http.Controller):
#     @http.route('/safeer_report_invoice/safeer_report_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/safeer_report_invoice/safeer_report_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('safeer_report_invoice.listing', {
#             'root': '/safeer_report_invoice/safeer_report_invoice',
#             'objects': http.request.env['safeer_report_invoice.safeer_report_invoice'].search([]),
#         })

#     @http.route('/safeer_report_invoice/safeer_report_invoice/objects/<model("safeer_report_invoice.safeer_report_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('safeer_report_invoice.object', {
#             'object': obj
#         })
