# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

from logging import getLogger

_logger = getLogger(__name__)

class AccountMoveLineLi(models.Model):
    _inherit = 'account.move.line'

    @api.model_create_multi
    def create(self, vals_list):
        iqd_currency = self.env.ref('base.IQD', raise_if_not_found=False)
        _logger.info(
                "iqd_currencyiqd_currencyiqd_currency %s"
                % iqd_currency
            )
        if not iqd_currency:
            raise ValidationError("IQD currency must exist in the system.")

        company_currency = self.env.company.currency_id
        for vals in vals_list:
            _logger.info(
                "vals.get('debit') %s"
                % vals.get('debit')
            )
            _logger.info(
                "vals.get('credit') %s"
                % vals.get('credit')
            )
            # Only apply if currency is not set and company currency is USD
            if company_currency.name == 'USD':
                # Get the exchange rate for the journal entry date
                move_date = vals.get('date') or fields.Date.context_today(self)
                rate = iqd_currency.with_context(date=move_date).rate or 0.0
                _logger.info(
                    "raterateraterateraterateraterate %s"
                    % rate
                )
                if rate > 0.0:
                    usd_to_iqd = rate
                    _logger.info(
                        "vals.get('usd_to_iqdusd_to_iqdusd_to_iqdusd_to_iqd') %s"
                        % usd_to_iqd
                    )
                    amount = vals.get('debit') or vals.get('credit') or 0.0
                    _logger.info(
                        "amount###################### %s"
                        % amount
                    )
                    vals['currency_id'] = iqd_currency.id

                    if vals.get('credit') > 0:
                        amount = -abs(vals.get('credit')) 
                        vals['amount_currency'] = round(amount * usd_to_iqd, 3)

                    if vals.get('debit') > 0:
                        amount = abs(vals.get('debit')) 
                        vals['amount_currency'] = round(amount * usd_to_iqd, 3)    

                    _logger.info(
                        "round(amount * usd_to_iqd, 3) %s"
                        % (round(amount * usd_to_iqd, 3))
                    )

        return super(AccountMoveLineLi, self).create(vals_list)         
    
# from odoo import models, fields, api


# class saffer2_accounts(models.Model):
#     _name = 'saffer2_accounts.saffer2_accounts'
#     _description = 'saffer2_accounts.saffer2_accounts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
