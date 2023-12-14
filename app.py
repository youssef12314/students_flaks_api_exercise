from flask import Flask, request, jsonify
from models import db, Student
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# Create a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'], grade=data.get('grade'))
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

# Get a single student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

# Update a student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    student.grade = data.get('grade', student.grade)
    db.session.commit()
    return jsonify(student.to_dict())

# Delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
