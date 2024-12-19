from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Result(models.Model):
    _name = 'ensa.result'
    _description = 'Result'

    student_id = fields.Many2one('ensa.student', string='Student', required=True)
    exam_id = fields.Many2one('ensa.exam', string='Exam', required=True)
    grade = fields.Float(string='Grade', required=True)
    status = fields.Selection([
        ('admitted', 'Admitted'),
        ('retake', 'Retake'),
        ('failed', 'Failed'),
    ], string='Status', compute='_compute_status', store=True)

    # Add related field for teacher_id
    teacher_id = fields.Many2one('ensa.teacher', string='Teacher', related='exam_id.teacher_id', store=True)

    @api.constrains('grade')
    def _check_grade_range(self):
        for record in self:
            if not (0 <= record.grade <= 20):
                raise ValidationError('Grade must be between 0 and 20.')
