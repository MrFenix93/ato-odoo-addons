from odoo import api, fields, models
from odoo.exceptions import AccessError


class AccountingCommonPartnerReport(models.TransientModel):
    _inherit = 'account.common.partner.report'

    result_selection = fields.Selection(
        selection='_get_result_selection',
        string="Partner's",
        required=True,
        default=lambda self: self._default_result_selection(),
    )

    @api.model
    def _default_result_selection(self):
        user = self.env.user

        has_ar = user.has_group('account_ar_ap_roles.group_account_ar_user')
        has_ap = user.has_group('account_ar_ap_roles.group_account_ap_user')

        if has_ar and not has_ap:
            return 'customer'

        if has_ap and not has_ar:
            return 'supplier'

        return 'customer'

    @api.model
    def _get_result_selection(self):
        user = self.env.user

        is_manager = user.has_group('account.group_account_manager')
        is_advisor = user.has_group('account.group_account_readonly')

        has_ar = user.has_group('account_ar_ap_roles.group_account_ar_user')
        has_ap = user.has_group('account_ar_ap_roles.group_account_ap_user')

        if is_manager or is_advisor or (has_ar and has_ap):
            return [
                ('customer', 'Receivable Accounts'),
                ('supplier', 'Payable Accounts'),
                ('customer_supplier', 'Receivable and Payable Accounts'),
            ]

        if has_ar:
            return [
                ('customer', 'Receivable Accounts')
            ]

        if has_ap:
            return [
                ('supplier', 'Payable Accounts')
            ]

        raise AccessError("You do not have access to this report.")