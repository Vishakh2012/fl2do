from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, BooleanField
from wtforms.validators import InputRequired

from fl import create_app


db=SQLAlchemy()
app = create_app()
app.config.from_pyfile('config.py')



class task_form(FlaskForm):
    task = StringField('enter your task',validators = [InputRequired('please enter the task')])
    task_desc = StringField('decribe your task briefly')
    sub_task1 = StringField('enter the subtask',validators = [InputRequired('please enter the task')])
    sub_task2 = StringField('enter the subtask',validators = [InputRequired('please enter the task')])
    sub_task3 = StringField('enter the subtask',validators = [InputRequired('please enter the task')])
    submit = SubmitField('Submit')
 


       


class Todo(db.Model):
    SNo= db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100),nullable=False)
    task_desc = db.Column(db.String(200),nullable=False)
    sub_task1 = db.Column(db.String(200),nullable=False)
    sub_task2 = db.Column(db.String(200),nullable=False)
    sub_task3 = db.Column(db.String(200),nullable=False)
    declared_at = db.Column(db.DateTime, default=datetime.utcnow)
    


class subtask(FlaskForm):
    cst1 = BooleanField("form.sub_task1.data",default = False)
    cst2 = BooleanField("form.sub_task2.data",default = False)
    cst3 = BooleanField("form.sub_task3.data",default = False)


@app.route("/")
def task():
    sub_form = subtask()
    form = task_form()
    allTodo = Todo.query.all()
    return render_template("index.html", form = form,allTodo=allTodo,sub_form=sub_form)
        
@app.route("/delete/<int:sno>", methods=["POST","GET"])
def delete_to_table(sno):
    del_task = Todo.query.filter_by(SNo = sno).first()
    db.session.delete(del_task)
    db.session.commit()
    return redirect("/")
    
    
    
    
    
    
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

