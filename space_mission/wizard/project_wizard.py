from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    _name = 'space.mission.project.wizard'
    _description = 'Wizard: Quick Project for Mission Object.'

    def _default_mission(self):
        return self.env['space_mission.mission'].browse(self._context.get('active_id'))
    def _default_name(self):
        return self.env['space_mission.mission'].browse(self._context.get('active_id')).name
    def _default_launch_date(self):
        return self.env['space_mission.mission'].browse(self._context.get('active_id')).launch_date
    def _default_return_date(self):
        return self.env['space_mission.mission'].browse(self._context.get('active_id')).return_date

    mission_id = fields.Many2one(comodel_name= 'space_mission.mission',
                               string='Mission',
                               required = True,
                               default=_default_mission)
    
    name = fields.Char(string="Project Name",
                      default=_default_name)

    mission_captain_id = fields.Many2one(comodel_name='res.users',
                                         string='Captain of the current mission',
                                         related='mission_id.captain_id',
                                         help='This is the Captain of the current session')
    
    mission_launch_date = fields.Datetime(string="This is the Mission Launch Date",
                                          default=_default_launch_date)
    
    mission_return_date = fields.Datetime(string="This is the Mission Return Date",
                                         default=_default_return_date)


    def create_project(self):
        project_id = self.env['project.project'].create({
            'name': self.name,
            'user_id': self.mission_captain_id.id,
            'mission_id': self.mission_id.id,
            'date_start': self.mission_launch_date,
            'date': self.mission_return_date,
        })