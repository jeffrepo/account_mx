# -*- coding: utf-8 -*-
{
    'name': "account_mx",

    'summary': """ Conta extra para MX """,

    'description': """
        Conta extra para MX
    """,

    'author': "JS",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['account','base'],

    'data': [
        'views/report.xml',
        'views/account_gt_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_view.xml',
        'report/reporte_libro_bancos_views.xml',
        'report/reporte_libro_conciliacion_bancaria_views.xml',
        'wizard/libro_bancos_wizard_views.xml',
        'wizard/libro_conciliacion_bancaria_wizard_views.xml',
        'wizard/conciliacion_bancaria_wizard_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'license': 'LGPL-3',
}
