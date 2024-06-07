=== Student Grade Management System ===

This project is a Student Grade Management System built with Flask.

=== Prerequisites ===

- Python 3.x installed on your system
- MySQL installed and running
- Virtual environment (optional but recommended)

=== Installation ===

1. Clone the repository:

    git clone https://github.com/tu_usuario/nombre_del_repositorio.git

2. Navigate to the project directory:

    cd nombre_del_repositorio

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
