from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField



db=SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fl2do.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY']= '6716c1c7a2a42caadadb169af7cc9df4'

class task_form(FlaskForm):
    task = StringField('enter your task')
    task_desc =StringField('decribe your task briefly')
    sub_task1 =StringField('enter the subtask')
    sub_task2 =StringField('enter the subtask')
    sub_task3 =StringField('enter the subtask')
    submit = SubmitField('Submit')
 
    

with app.app_context():
    db.init_app(app)

class Todo(db.Model):
    SNo= db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100),nullable=False)
    task_desc = db.Column(db.String(200),nullable=False)
    sub_task1 = db.Column(db.String(200),nullable=False)
    sub_task2 = db.Column(db.String(200),nullable=False)
    sub_task3 = db.Column(db.String(200),nullable=False)
    declared_at = db.Column(db.DateTime, default=datetime.utcnow)
    



@app.route("/")
def task():
    form = task_form()
    allTodo = Todo.query.all()
    return render_template("index.html", form = form,allTodo=allTodo)
        
@app.route("/update/", methods=["POST","GET"])
def add_to_table():
    form = task_form()
    if request.method == 'POST' and form.validate_on_submit():
        todo = Todo(
            task_name = form.task.data,
            task_desc = form.task_desc.data,
            sub_task1 = form.sub_task1.data,
            sub_task2 = form.sub_task2.data,
            sub_task3 = form.sub_task3.data
            )
        db.session.add(todo)
        db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True,use_reloader = False)
