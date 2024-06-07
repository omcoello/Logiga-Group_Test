import datetime
from flask import Blueprint, render_template, request, jsonify
from .models import Student, Subject, Grade
from .database import SQLAlchemySingleton
# from .serializer import serialize_model_instance
from sqlalchemy.exc import IntegrityError

db = SQLAlchemySingleton.get_instance()

main = Blueprint('main',__name__)
products_bp = Blueprint('products', __name__, url_prefix='/products')   


@main.route('/students/grades', methods=['GET'])
def get_students_grades():
    students = Student.query.all()
    result = []

    for student in students:
        student_name = f"{student.first_name} {student.last_name}"
        student_grades = {f"{student_name}": {"term1": None, "term2": None, "term3": None, "averageGrade": None, "result": None}}
        
        grades = Grade.query.filter_by(student_id=student.id).all()
        term_grades = {1: None, 2: None, 3: None}
        
        for grade in grades:
            term_grades[grade.term] = grade.grade

        average_grade = None
        if None not in term_grades.values():
            average_grade = sum(term_grades.values()) / 3
        
        student_grades[student_name]["term1"] = term_grades[1]
        student_grades[student_name]["term2"] = term_grades[2]
        student_grades[student_name]["term3"] = term_grades[3]
        student_grades[student_name]["averageGrade"] = average_grade
        student_grades[student_name]["result"] = "Failed" if average_grade is not None and average_grade < 15 else "Approved" if average_grade is not None else None

        result.append(student_grades)

    return jsonify(result), 200

@main.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(
        first_name=data['first_name'],
        last_name=data['last_name'],
        birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d').date(),
        guardian=data['guardian']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created successfully'}), 201

@main.route('/subjects', methods=['POST'])
def create_subject():
    data = request.get_json()
    new_subject = Subject(
        name=data['name'],
        description=data['description']
    )
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Subject created successfully'}), 201

@main.route('/grades', methods=['POST'])
def create_or_update_grade():
    data = request.get_json()
    student_id = data['student_id']
    subject_id = data['subject_id']
    term = data['term']
    grade_value = data['grade']
    
    grade = Grade.query.filter_by(student_id=student_id, subject_id=subject_id, term=term).first()
    
    if grade:
        grade.grade = grade_value
        message = 'Grade updated successfully'
    else:
        grade = Grade(
            student_id=student_id,
            subject_id=subject_id,
            term=term,
            grade=grade_value
        )
        db.session.add(grade)
        message = 'Grade created successfully'
    
    db.session.commit()
    return jsonify({'message': message}), 201
