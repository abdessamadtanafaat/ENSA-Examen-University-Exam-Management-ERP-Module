{
    'name': 'ENSA Exam Management',
    'version': '1.0',
    'author': 'Abdessamad',
    'category': 'Education',
    'description': 'Manage exams, students, and results.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/exam_view.xml',
        'views/result_view.xml',
        'views/room_view.xml',
        'views/menu_views.xml',
        'views/subject_view.xml',
        'views/teacher_view.xml',
    ],
    'test': [
    'tests/test_exam_management.py',
    ],

    'installable': True,
    'application': True,
}
