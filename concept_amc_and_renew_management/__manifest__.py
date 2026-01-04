{
    'name': 'AMC & Renewal Management',
    'version': '1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Manage Annual Maintenance Contracts (AMC) and Renewals',
    'author': 'Concept Solutions LLC',
    'company': 'Concept Solutions LLC',
    'website': 'https://www.csloman.com',
    'maintainer': 'Concept Solutions LLC',
    'description': """
        AMC Management module helps you:
        - Manage AMCs
        - Auto generate quotations
        - Integrate with CRM and Sales
        """,
    'depends': [
        'base',
        'project',
        'mail',
        'crm',
        'sale_management',
        'stock',
        'account',
        'sale_crm',
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/amc_dashboard.xml',
        'views/sale_views.xml',
        'views/crm_views.xml',
        'views/account_move_view.xml',
        'wizard/amc_link_wizard.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'concept_amc_and_renew_management/static/src/css/amc_hide_label.css',
        ],
    },
    # Store Configuration
    'price': 110.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'images': ['static/description/banner.png'], # Recommended: Ensure you have a banner
    'installable': True,
    'auto_install': False,
    'application': True,
}
