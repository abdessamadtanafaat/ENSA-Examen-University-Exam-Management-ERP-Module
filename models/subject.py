from odoo import models, fields

class Subject(models.Model):
    _name = 'ensa.subject'
    _description = 'Subject'

    name = fields.Char(string='Subject Name', required=True)
    module = fields.Char(string='Module')
    student_ids = fields.Many2many('ensa.student', string="Students")
