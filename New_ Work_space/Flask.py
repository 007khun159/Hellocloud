from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,VARCHAR,CHAR



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:YKQnti46682@10.104.9.211:5432/workspace'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db = SQLAlchemy(app)


class Students(db.Model):
    tablename  = 'Students'
    id = Column(CHAR(13),primary_key = True)
    f_name = Column(VARCHAR(30))
    l_name = Column(VARCHAR(30))
    e_mail = Column(VARCHAR(50))

     
@app.route('/')
def index():
    result = Students.query.all()
    return render_template('index.html',result = result)


@app.route('/process',methods =['Post'])
def process():
    id = request.form['student_id']
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    e_mail = request.form['e_mail']
    signature = Students(id=id , f_name = f_name , l_name = l_name , e_mail = e_mail)
    db.session.add(signature)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    
     app.run(host = '0.0.0.0',port = 80,debug = True)