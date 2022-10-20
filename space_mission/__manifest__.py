{
    'name': 'Space Mission',
    'version': '0.6',
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
    
    'depends': ['project','website'],
    'data': [
        'security/space_mission_groups.xml',
        'security/space_mission_security.xml',
        'security/ir.model.access.csv',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml',
        'views/mission_views.xml',
        'views/space_mission_web_templates.xml',
        'report/mission_report_template.xml',
        'views/project_views_inherit.xml',
        'wizard/project_wizard.xml',
    ],
    'demo': ['demo/spaceship_demo.xml',],
    
    'assets': {},
    
    'installable': True,
    'application': True,
    'auto_install': False,
    
}

