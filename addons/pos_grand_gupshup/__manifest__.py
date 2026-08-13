{
    'name': 'Grand Gup Shup POS',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Custom POS setup and styling for Grand Gup Shup Restaurant',
    'depends': ['point_of_sale'],
    'data': [
        'data/pos_categories.xml',
        'data/product_attributes.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_grand_gupshup/static/src/scss/pos_theme.scss',
        ],
    },
    'post_init_hook': '_setup_menu_data',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
