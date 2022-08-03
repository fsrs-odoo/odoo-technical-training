from odoo import fields, models


class Dog(models.Model):
    _name = "dog.dog"
    name = fields.Char(name="Breed")
