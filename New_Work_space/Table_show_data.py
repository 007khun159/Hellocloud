from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Database_orm  import Student,Teachers,Subjects,Registration,session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:YKQnti46682@10.104.9.211:11256/newingwork_space'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db = SQLAlchemy(app)

@app.route('/')
def index():
    result = session.query(Student.student_id,Student.f_name,Registration.subject_id,Subjects.subject_name,Registration.grade,Teachers.f_tname,Teachers.l_tname)\
        .outerjoin(Registration,Student.student_id == Registration.student_id)\
        .outerjoin(Subjects,Registration.subject_id == Subjects.subject_id).join(Teachers,Subjects.teacher_id == Teachers.teacher_id).all()
    return render_template('index.html',result = result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
     