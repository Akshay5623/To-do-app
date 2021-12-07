from application import app, db
from application.models import Tasks
from flask import render_template

@app.route('/')
def home():
    all_tasks = Tasks.query.all() # retrieve a list of tasks from the db
    return render_template("index.html", title="Home", all_tasks=all_tasks) # all_tasks=all_tasks will be used to show the tasks on the webpage in conjunction with the for loop in index.html

@app.route('/create_task')
def create_task():
    new_task = Tasks(description="New Task")
    db.session.add(new_task)
    db.session.commit()
    return f"Task added with ID {new_task.id}"
# Don't need to add id as its auto incremented, don't need to add completed as it already has a default value
# db.session.add adds the new task and db.session.commit commits the input to the database