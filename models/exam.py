from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Exam(models.Model):
    _name = 'ensa.exam'
    _description = 'Exam'

    name = fields.Char(string='Exam Name', required=True)
    type = fields.Selection([('ds', 'DS'), ('final', 'Final'), ('retake', 'Retake')], string='Exam Type', required=True)
    date = fields.Date(string='Exam Date', required=True)
    room_id = fields.Many2one('ensa.room', string='Room')
    teacher_id = fields.Many2one('ensa.teacher', string='Teacher')
    subject_id = fields.Many2one('ensa.subject', string='Subject', required=True)
    student_ids = fields.Many2many('ensa.student', string='Students')

    @api.constrains('student_ids')
    def _check_student_enrollment_in_subject(self):
        for exam in self:
            for student in exam.student_ids:
                if exam.subject_id not in student.subject_ids:
                    raise ValidationError(f"Student {student.name} is not enrolled in the subject {exam.subject_id.name} and cannot be registered for this exam.")
