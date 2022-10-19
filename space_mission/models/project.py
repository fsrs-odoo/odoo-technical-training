from odoo import api, fields, models

class Project(models.Model):
    _inherit = "project.project"
    
    mission_id = fields.Many2one(comodel_name='space_mission.mission',
                                 string="Mission")
    user_id = fields.Many2one(string='Mission Captain')
