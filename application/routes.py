from application import app, db
from application.models import Tasks
from application.forms import TaskForm
from flask import render_template, request, url_for, redirect

@app.route('/')
def home():
    all_tasks = Tasks.query.all() # retrieve a list of tasks from the db
    return render_template("index.html", title="Home", all_tasks=all_tasks) # all_tasks=all_tasks will be used to show the tasks on the webpage in conjunction with the for loop in index.html

@app.route('/create_task', methods=["GET","POST"])
def create_task():
    form = TaskForm()
    
    if request.method == "POST":
        new_task = Tasks(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home")) # home here is the name of the function not the name of the route
    
    return render_template("create_task.html", title="Add a Task", form=form)

#    return f"Task added with ID {new_task.id}"
# Don't need to add id as its auto incremented, don't need to add completed as it already has a default value
# db.session.add adds the new task and db.session.commit commits the input to the database