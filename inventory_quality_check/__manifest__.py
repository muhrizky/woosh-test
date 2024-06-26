{
    'name': 'Inventory Quality Check',
    'version': '14.0.1.0.0',
    'category': 'Inventory',
    'author': 'Muhammad Rizqi',
    'license': 'AGPL-3',
    'summary': 'Customizations for the Inventory Quality Check',
    'description': 'Adds a custom field and enhances workflow and UI for Inventory module',
    'depends': ['stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'inventory_quality_check/static/src/css/inventory_custom.css',
        ],
    },
    'installable': True,
    'auto_install': False,
}

