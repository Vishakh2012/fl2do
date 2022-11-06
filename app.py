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
    sub_task1 =StringField('sub_task1')
    sub_task2 =StringField('sub_task2')
    sub_task3 =StringField('sub_task3')
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
    



@app.route("/update/", methods=["POST","GET"])
def task():
    form = task_form()
    if form.validate_on_submit():
        return redirect("/success/")
    return render_template("index.html", form = form)
        
@app.route("/success/")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True,use_reloader = False)
