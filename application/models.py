from application import db

# represents the tasks table in database. db_Model is where we inherit the methods and functionalities from in regards to db
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    