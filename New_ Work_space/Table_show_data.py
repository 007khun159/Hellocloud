from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,VARCHAR,CHAR
from Database_orm  import Student,Teachers,Subjects,Registration,session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:YKQnti46682@10.104.9.211:5432/newingwork_space'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False



@app.route('/')
def index():
    result = session.query(Student.student_id,Student.f_name,Student.l_name,Student.email).all()
    return render_template('index.html',result = result)





if __name__ == "__main__":
    
    app.run(host = '0.0.0.0',port = 80,debug = True)
     