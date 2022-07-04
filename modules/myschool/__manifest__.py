{
    'name': 'MySchool',
    'version': '1.0',
    'category': 'School/myschool',
    'sequence': -10,
    'summary': 'MySchool Manage',
    'description': "MySchool description",
    'author':'present',
    'data': [
        'views/school_view.xml',
        'views/class_view.xml',
        'views/student_view.xml',
        'security/ir.model.access.csv'
    ],
    # 'depends':['myclass'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
