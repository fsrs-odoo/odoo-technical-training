from odoo import fields, models


class Dog(models.Model):
    _name = "dog.dog"
    _description = "Many Dogs"
    breed = fields.Char(name="Breed")
    parent_id = fields.Many2one("dog.dog", string="Parent", ondelete="cascade")
