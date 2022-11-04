
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm


db=SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fl2do.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY']= '6716c1c7a2a42caadadb169af7cc9df4'

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
def show():
    allTodo = Todo.query.all()
    return render_template('index.html',allTodo = allTodo)

@app.route("/update/", methods=["POST","GET"])
def create_task():
    if request.method == 'POST':
        task_name = request.form["task_name"]
        task_desc = request.form["task_desc"]
        sub_task1 = request.form["sub_task1"]
        sub_task2 = request.form["sub_task2"]
        sub_task3 = request.form["sub_task3"]
        
        todo = Todo(
            task_name=task_name,
            task_desc=task_desc,
            sub_task1 = sub_task1,
            sub_task2 = sub_task2,
            sub_task3 = sub_task3
            )
        db.session.add(todo)
        db.session.commit()
    return redirect("/")
        

if __name__ == "__main__":
    app.run(debug=True)

