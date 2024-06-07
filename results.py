from .views import get_students_grades

def print_students_grades():
    json_result = get_students_grades()[0]
    for student_data in json_result:
        print(f"Student: {student_data['Student']}")
        print("Grades:")
        for grade_data in student_data['Grades']:
            print(f"  Term {grade_data['Term']}: {grade_data['Grade']}")
        print(f"Average Grade: {student_data['AverageGrade']}")
        print(f"Result: {student_data['Result']}\n")

print_students_grades()