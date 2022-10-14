{
    'name': 'Space Mission',
    'version': '0.3',
    'summary': 'Odoo Application to control its Space Mission',
    'description': """
        Space Mission Application to Manage Space Control:
            -
            -
            -
        """,
    'license': 'OPL-1',
    'author': 'fsrs-odoo',
    'website': 'www.odoo.com',
    'category': 'Tech Training',
    
    'depends': ['base'],
    'data': [
        'security/space_mission_groups.xml',
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml'
    ],
    'demo': ['demo/spaceship_demo.xml',],
    
    'assets': {},
    
    'installable': True,
    'application': True,
    'auto_install': False,
    
}

