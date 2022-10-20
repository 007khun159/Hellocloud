from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:YKQnti46682@10.104.9.211:5432/Work'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    student_id = Column(String(13), primary_key=True)
    f_name = Column(String(60), nullable=False)
    l_name = Column(String(60), nullable=False)
    email = Column(String(50), nullable=False)

    def __init__(self,student_id,f_name,l_name,email):
        self.student_id = student_id 
        self.f_name = f_name
        self.l_name = l_name
        self.email = email


data1 = Student('6406022610031','Papop','Sangeamsak','s6406022610031@fitm.kmutnb.ac.th')




if __name__ == "__main__":
    
    app.run(host = '0.0.0.0',port = 80,debug = True)