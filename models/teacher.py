from odoo import models, fields

class Teacher(models.Model):
    _name = 'ensa.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    specialty = fields.Char(string='Specialty')
