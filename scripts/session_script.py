from xmlrpc import client

url = 'https://april-odoo-technical-training-15-0-odoo-academy-day1-4574083.dev.odoo.com'
db = 'april-odoo-technical-training-15-0-odoo-academy-day1-4574083'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'academy.session', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)

courses = models.execute_kw(db, uid, password,
                           'academy.course', 'search_read',
                           [[['level', 'in', ['intermediate', 'beginner']]]])
print(courses)

course = models.execute_kw(db, uid, password,
                          'academy.course', 'search',
                          [[['name', '=', 'Accounting 200']]])

session_fields = models.execute_kw(db, uid, password,
                                  'academy.session', 'fields_get',
                                  [],{'attributes': ['string', 'type', 'required']})
print(session_fields)

new_session = models.execute_kw(db, uid, password,
                               'academy.session', 'create',
                               [
                                   {
                                       'course_id': course[0],
                                       'state': 'open',
                                       'duration': 5,
                                   }
                               ]
                               )
print(new_session)