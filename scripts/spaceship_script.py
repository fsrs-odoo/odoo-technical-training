from xmlrpc import client

url = 'https://october-technical-training-15-0-space-mission-6156500.dev.odoo.com'
db = 'october-technical-training-15-0-space-mission-6156500'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'space_mission.spaceship', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)

spaceship_fields = models.execute_kw(db, uid, password,
                                  'space_mission.spaceship', 'fields_get',
                                  [],{'attributes': ['string', 'type', 'required']})
print(spaceship_fields)

new_spaceship = models.execute_kw(db, uid, password,
                               'space_mission.spaceship', 'create',
                               [
                                   {
                                       'name': 'Millenium Falcon',
                                       'type': 'freighter',
                                       'model': 'YT-1300F light freighter',
                                       'crew_capacity': 30,
                                       'length': 114,
                                       'width': 94,
                                       'height': 26,
                                       'fuel_type': 'solid_fuel',
                                   }
                               ]
                               )
print(new_spaceship)
