import sqlalchemy
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
import uuid


Engine = sqlalchemy.create_engine('sqlite:/// Workspace.sqlite3')
Base = declarative_base()


#Student Class 
class Student(Base):
    __tablename__ = 'students'
    
    student_id = Column(String(13),primary_key = True ,nullable = False)
    f_name = Column(String(60),nullable = False)
    l_name = Column(String(60), nullable = False)
    email = Column(String(50),nullable = False)
    

    def __repr__(self):
        return "<User(student_id ='%s',f_name = '%s',l_name = '%s')>"%(
            self.student_id , self.f_name , self.l_name)


#Teachers Class
class Teachers(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(String(3),primary_key = True )
    f_name = Column(String(20), nullable = False)
    l_name  = Column(String(20),nullable = False)
    email = Column(String(50),nullable = False)

    

    def __repr__(self):
        return "<User(teacher_id ='%s',f_name = '%s',l_name = '%s')>"%(
            self.teacher_id , self.f_name , self.l_name)
    

#Subject Class 

class Subjects(Base):
    __tablename__ = 'subjects'
    subject_id = Column(String(15), primary_key = True)
    subject_name = Column(String(50),nullable = False)
    creadit = Column(Integer,nullable = False)
    teacher_id = Column(String(3),nullable = False)


    def __repr__(self):
        return "<User(subject_id ='%s',subject_name = '%s',creadit = '%s',teacher_id = '%s')>"%(
            self.subject_id , self.subject_id , self.creadit , self.teacher_id)


Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)

Engine_start = sessionmaker(bind= Engine)
session = Engine_start()
session.add()

session.commit()