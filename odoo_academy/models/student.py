# .*. coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = "academy.student"
    _description = "Course Student of Odoo Academy"
    _inherits = {
        
        'res.partner': 'partner_id',
    }
    
        
    partner_id = fields.Many2one(comodel_name="res.partner",
                                delegate=True,
                                ondelete="cascade",
                                required=True)
    #SEQUENCE FIELD
    enrollment_number =fields.Char(string='Enrollment Number', readonly=True, required=True, copy=False, index=True, default='AB000000000')
    
    session_ids = fields.Many2many(string="Enrolled Sessions", comodel_name="academy.session")
    
    #OVERIDE CREATE FUNCTION
    @api.model
    def create(self, vals):
        if vals.get('enrollment_number','AB000000000')=='AB000000000':
            vals['enrollment_number'] = self.env['ir.sequence'].next_by_code(
            'enrollment_sequence') or _('AB000000000')
            result = super().create(vals)
            return result