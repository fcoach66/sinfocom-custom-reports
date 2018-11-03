{
    'name': 'Sinfocom Sale Order Report',
    'version': '1.0',
    'category': 'Localization/Italy',
    'sequence': 14,
    'summary': '',
    'description': """
Sale Order / Quotation Report for Sinfocom
    """,
    'author':  'fcoach66',
    'website': 'www.cocciari.com',
    'images': [
    ],
    'depends': [
        'sale',
        'sales_team',
		'account',
		'portal',
		'sale_additional_text_template',
        'sale_mandatory_fields',
        'sinfocom_common_reports',
	],
    'data': [
        'report/sale_report_templates.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
