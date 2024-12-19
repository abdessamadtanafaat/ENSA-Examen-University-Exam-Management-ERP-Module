from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'ensa.student'
    _description = 'Student'

    name = fields.Char(string='Full Name', required=True)
    registration_number = fields.Char(string='Registration Number', required=True)
    semester = fields.Selection([('sem1', 'Semester 1'), ('sem2', 'Semester 2')], string='Semester', required=True)
    subject_ids = fields.Many2many('ensa.subject', string='Enrolled Subjects')

    @api.constrains('subject_ids')
    def _check_subject_enrollment(self):
        if not self.subject_ids:
            raise ValidationError("A student must be enrolled in at least one subject.")
