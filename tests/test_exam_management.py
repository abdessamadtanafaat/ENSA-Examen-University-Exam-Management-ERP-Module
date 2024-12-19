from odoo.tests import TransactionCase
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError



class TestExamModule(TransactionCase):

    # Test the Student Registration to an Exam
    def test_student_registration(self):
        # Create a student
        student = self.env['ensa.student'].create({
            'name': 'John Doe',
            'registration_number': '123456',
            'semester': 'sem1',
        })
        
        # Create a subject and an exam (ensure student is registered)
        subject = self.env['ensa.subject'].create({
            'name': 'Mathematics',
        })
        exam = self.env['ensa.exam'].create({
            'name': 'Math Exam',
            'type': 'final',
            'date': '2024-12-20',
            'room_id': self.env.ref('ensa_examen.room_1'),
            'teacher_id': self.env.ref('ensa_examen.teacher_1'),
            'subject_id': subject.id,
        })
        
        # Try to register a student not enrolled in the subject
        with self.assertRaises(ValidationError):
            self.env['ensa.exam.registration'].create({
                'student_id': student.id,
                'exam_id': exam.id,
            })
        
        # Enroll the student in the subject
        student.subject_ids = [(4, subject.id)]
        
        # Now, try to register the student for the exam
        registration = self.env['ensa.exam.registration'].create({
            'student_id': student.id,
            'exam_id': exam.id,
        })
        self.assertTrue(registration)
        
    # Test Grade Validation (Grade should be between 0 and 20)
    def test_grade_entry(self):
        # Create a student and an exam
        student = self.env['ensa.student'].create({
            'name': 'John Doe',
            'registration_number': '123456',
            'semester': 'sem1',
        })
        exam = self.env['ensa.exam'].create({
            'name': 'Math Exam',
            'type': 'final',
            'date': '2024-12-20',
            'room_id': self.env.ref('ensa_examen.room_1'),
            'teacher_id': self.env.ref('ensa_examen.teacher_1'),
        })
        
        # Create a result with a valid grade
        result = self.env['ensa.result'].create({
            'student_id': student.id,
            'exam_id': exam.id,
            'grade': 15,
        })
        self.assertEqual(result.grade, 15)
        
        # Try to create a result with an invalid grade (>20)
        with self.assertRaises(ValidationError):
            self.env['ensa.result'].create({
                'student_id': student.id,
                'exam_id': exam.id,
                'grade': 25,
            })
        
        # Try to create a result with an invalid grade (<0)
        with self.assertRaises(ValidationError):
            self.env['ensa.result'].create({
                'student_id': student.id,
                'exam_id': exam.id,
                'grade': -5,
            })
        
    # Test Room Booking (Room cannot be double-booked at the same time)
    def test_room_booking(self):
        # Create an exam and a room
        room = self.env['ensa.room'].create({
            'name': 'Room 101',
            'capacity': 30,
        })
        exam_1 = self.env['ensa.exam'].create({
            'name': 'Math Exam',
            'type': 'final',
            'date': '2024-12-20 09:00:00',
            'room_id': room.id,
            'teacher_id': self.env.ref('ensa_examen.teacher_1'),
        })
        exam_2 = self.env['ensa.exam'].create({
            'name': 'History Exam',
            'type': 'final',
            'date': '2024-12-20 09:00:00',  # Same time
            'room_id': room.id,
            'teacher_id': self.env.ref('ensa_examen.teacher_2'),
        })
        
        # Try to create the second exam in the same room at the same time
        with self.assertRaises(ValidationError):
            self.env['ensa.exam'].create({
                'name': 'History Exam',
                'type': 'final',
                'date': '2024-12-20 09:00:00',
                'room_id': room.id,
                'teacher_id': self.env.ref('ensa_examen.teacher_2'),
            })
