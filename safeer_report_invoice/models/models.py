# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SafeerInvoic(models.Model):
    _inherit = "account.move"

    name_to = fields.Char("Name To")
    name_from = fields.Char("Name From")

# class safeer_report_invoice(models.Model):
#     _name = 'safeer_report_invoice.safeer_report_invoice'
#     _description = 'safeer_report_invoice.safeer_report_invoice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
