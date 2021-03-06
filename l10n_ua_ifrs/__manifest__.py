# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Ukraine - Accounting IFRS",
    'author': "ERP Ukraine",
    'website': "https://erp.co.ua",
    'version': '1.5',
    'license': 'Other proprietary',
    'description': """
Ukrainian accounting based on IFRS rules
=========================================
    """,
    'category': 'Localization',
    'depends': ['account', 'l10n_ua'],
    'data': [
        'data/account_chart_template.xml',
        'data/account.account.template.csv',
        'data/account_tax_template.xml',
        'data/account_chart_template_config.xml',
        'data/account_chart_template_data.xml',
    ],
    'auto_install': False,
}
