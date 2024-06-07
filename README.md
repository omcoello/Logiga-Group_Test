=== Student Grade Management System ===

This project is a Student Grade Management System built with Flask.

=== Prerequisites ===

- Python 3.x installed on your system
- MySQL installed and running
- Virtual environment (optional but recommended)

=== Installation ===

1. Clone the repository:

    git clone https://github.com/omcoello/Logiga-Group_Test.git

2. Navigate to the project directory (follow this command in case you didn't specify a different directory repo name):

    cd Logiga-Group_Test

3. Create and activate a virtual environment (optional but recommended):

    python -m venv venv
    . venv/bin/activate  (for Unix/Linux)
    . venv\Scripts\activate  (for Windows)

4. Install dependencies:

    pip install -r requirements.txt

5. Set up the environment variables:

    Create a file named .env in the root directory of the project and add the following variables:
    
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=studentGradeDB
    DB_USER=your_username
    DB_PASSWORD=your_password
    FLASK_APP=app.py
    FLASK_ENV=development

6. Initialize the database:

    flask db init
    flask db migrate
    flask db upgrade

=== Running the Application ===

Once you have completed the installation steps:

1. Ensure your MySQL server is running.

2. Run the Flask application:

    flask run

3. Access the application in your web browser at http://localhost:5000.

=== Printing Student Grades ===

The `results.py` file contains a Python function `print_students_grades()` that retrieves student grades from the API endpoint and prints them to the console. The function calls `get_students_grades()` to fetch the data and then iterates through the JSON result to print each student's grades, average grade, and result.

To execute this code successfully, make sure to follow these steps:

1. Ensure that the Flask server is running to provide the API endpoint.
2. Execute the `results.py` file in your Python environment.
3. The `print_students_grades()` function will then be called automatically, fetching the data from the API and printing it to the console.

```python
# Example usage to print student grades
print_students_grades()



=== SQL queries solution ===

The `script_solution.sql` file contains a SQL script with solutions to specific queries. These queries are designed to retrieve data from the `persona` table according to various criteria such as age, gender, musical preference, and artistic preference. Each query is numbered and accompanied by a brief description of its purpose. These SQL queries can be executed in a MySQL environment to analyze and extract relevant information from the dataset.


=== API Endpoints ===

- GET /students/grades
    Retrieves grades for all students in JSON format.

- POST /students
    Creates a new student.
    Request body should be a JSON object with the following keys:
        - first_name (string): First name of the student.
        - last_name (string): Last name of the student.
        - birth_date (string): Date of birth of the student in the format 'YYYY-MM-DD'.
        - guardian (string): Name of the student's guardian.

- POST /subjects
    Creates a new subject.
    Request body should be a JSON object with the following keys:
        - name (string): Name of the subject.
        - description (string): Description of the subject.

- POST /grades
    Creates or updates a grade for a student in a subject.
    Request body should be a JSON object with the following keys:
        - student_id (integer): ID of the student.
        - subject_id (integer): ID of the subject.
        - term (integer): Term number (1, 2, or 3).
        - grade (float): Grade value for the student in the subject.

=== Additional Notes ===

- Make sure to replace "your_username" and "your_password" in the .env file with your MySQL username and password respectively.

- You may need to adjust the database configuration in config.py if you're not using MySQL or if your MySQL setup differs from the default configuration.

- For production use, remember to set FLASK_ENV=production in the .env file and configure your web server accordingly.

- For more information on how to use Flask, consult the official Flask documentation: https://flask.palletsprojects.com/en/2.0.x/
