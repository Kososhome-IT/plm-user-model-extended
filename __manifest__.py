{
    'name': 'User Extended Fields',
    'version': '1.0',
    'summary': 'Adds custom fields to res.users model',
    'category': 'Customizations',
    'author': 'your name',
    'depends': ['base','product','crm'],
    'data': [
        'views/res_users_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
