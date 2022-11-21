from odoo import fields, models


class Dog(models.Model):
    _name = "dog.dog"
    _description = "Many Dogs"
    name = fields.Char(name="Breed")
    size = fields.Selection(selection=[('xs','Mini Toy'),
                                       ('s','Small'),
                                       ('m','Medium'),
                                       ('l','Large'),
                                       ('xl','Giant')])
