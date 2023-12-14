from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(120))

    def __repr__(self):
        return '<Student %r>' % self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
