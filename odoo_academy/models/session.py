# .*. coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    course_id = fields.Many2one(comodel_name='academy.course',
                               string='Course',
                               ondelete='cascade',
                               required=True)

    name = fields.Char(string='Title', related='course_id.name')

    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor')

    student_ids = fields.Many2many(comodel_name='res.partner', string='Students')