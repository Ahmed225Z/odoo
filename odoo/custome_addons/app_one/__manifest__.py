{

    'name': 'app_one',

    'version': '1.0',

    'category': 'Uncategorized',

    'summary': 'App One',

    'description': """

        App One

    """,

    'author': 'Your Name',

    'depends': ['base'],

    'data': ['views/base_menu.xml','security/ir.model.access.csv','views/property_view.xml','views/owner_view.xml','views/tag_view.xml'],
    'assets': {
    'web.assets_backend': [
        'app_one/static/src/css/property.css',
    ],
    },
    'installable': True,

    'application': True,

    'auto_install': False,

}