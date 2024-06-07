from sqlalchemy.dialects.postgresql import ENUM
from .database import SQLAlchemySingleton

db = SQLAlchemySingleton.get_instance()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    guardian = db.Column(db.String(100), nullable=False)

    def __init__(self, first_name, last_name, birth_date, guardian):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.guardian = guardian

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    term = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Float, nullable=False)

    student = db.relationship('Student', backref=db.backref('grades', lazy=True))
    subject = db.relationship('Subject', backref=db.backref('grades', lazy=True))

    def __init__(self, student_id, subject_id, term, grade):
        self.student_id = student_id
        self.subject_id = subject_id
        self.term = term
        self.grade = grade
