import sqlalchemy
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
import uuid


Engine = sqlalchemy.create_engine('postgresql://webadmin:YKQnti46682@node36984-env-papop.proen.app.ruk-com.cloud:11256/testormdb')
Base = declarative_base()


#Student Class 
class Student(Base):
    __tablename__ = 'students'
    student_id = Column(String(13),primary_key = True ,nullable = False,unique = True)
    f_name = Column(String(60),nullable = False)
    l_name = Column(String(60), nullable = False)
    email = Column(String(50),nullable = False)
    regiss = relationship('Registration',backref = 'students')

    

    def __repr__(self):
        return "<User(student_id ='%s',f_name = '%s',l_name = '%s')>"%(
            self.student_id , self.f_name , self.l_name)


#Teachers Class
class Teachers(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(String(3),primary_key = True)
    f_tname = Column(String(20), nullable = False)
    l_tname  = Column(String(20),nullable = False)
    email = Column(String(50),nullable = False)
    subj = relationship('Subjects',backref = 'teachers')

    def __repr__(self):
        return "<User(teacher_id ='%s',f_name = '%s',l_name = '%s')>"%(
            self.teacher_id , self.f_name , self.l_name)
    

#Subject Class 

class Subjects(Base):
    __tablename__ = 'subjects'
    subject_id = Column(String(15), primary_key = True)
    subject_name = Column(String(50),nullable = False)
    creadit = Column(Integer,nullable = False)
    teacher_id = Column(String(3),ForeignKey('teachers.teacher_id'))
    


    def __repr__(self):
        return "<User(subject_id ='%s',subject_name = '%s',creadit = '%s',teacher_id = '%s')>"%(
            self.subject_id , self.subject_id , self.creadit , self.teacher_id)
    

class Registration(Base):
    __tablename__ = 'registration'
    id = Column(Integer,primary_key = True,nullable =False)
    student_id = Column(String(13),ForeignKey('students.student_id'))
    subject_id = Column(String(15),ForeignKey('subjects.subject_id'))
    year = Column(String(4),nullable = False)
    semester  = Column(String(2) ,nullable = False)
    grade  = Column(String(2),nullable   = False)


    
    def __repr__(self):
        return "<User(student_id ='%s',subject_id = '%s',year = '%s', semester = '%s',grade ='%s' )>"%(
            self.student_id , self.subject_id , self.year , self.semester,self.grade)



#Order information to start process
Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine) 

Engine_start = sessionmaker(bind= Engine)
session = Engine_start()




# Information 

student1 = Student(student_id = '6406022610031' , f_name = 'Papop', l_name  = 'Sangeamsak',email = '6406022610031@fitm.kmutnb.ac.th')
student2 = Student(student_id = '6406022610040',f_name = 'Pawarit',l_name = 'Pitirit',email = '6406022610040@fitm.kmutnb.ac.th')
student3 = Student(student_id = '6406022610032',f_name = 'Nititat',l_name = 'Banpha',email = '6406022610032@fitm.kmutnb.ac.th')

teacher1 = Teachers(teacher_id ='AMK',f_name = 'Anirach',l_name ='Mingkwan',email = 'Anirach@gmail.com')
teacher2 = Teachers(teacher_id ='WKN',f_name = 'Warachai',l_name ='Kongsiriwatana',email = 'Warachai@gmail.com')
teacher3 = Teachers(teacher_id ='KNM',f_name = 'Kanitta',l_name ='Namee',email = 'Kanitta@gmail.com')

subject1 = Subjects(subject_id = '060233113',subject_name = 'ADVANCED COMPUTER PROGRAMMIN', creadit =  3 ,teacher_id = 'AMK'  )
subject2 = Subjects(subject_id = '060233201',subject_name = 'NETWORK ENGINEERING LABORATO', creadit =  1 ,teacher_id = 'WKN' )
subject3 = Subjects(subject_id = '060233205',subject_name = 'ADVANCED NETWORK AND PROTOCO', creadit = 3 ,teacher_id = 'KNM' )

register1 = Registration(student_id = '6406022610031' , subject_id = '060233113', year = '2022' , semester =  '1',grade='+A')
register2 = Registration(student_id = '6406022610031' , subject_id = '060233201', year =  '2022' , semester =  '1',grade='C')
register3 = Registration(student_id = '6406022610040' , subject_id = '060233205', year = '2022' , semester =  '1',grade='B')
register4 = Registration(student_id = '6406022610040' , subject_id = '060233205', year = '2022' , semester =  '1',grade='A')
register5 = Registration(student_id = '6406022610032' , subject_id = '060233201', year = '2022' , semester =  '1',grade='+B')
register6 = Registration(student_id = '6406022610032' , subject_id = '060233113', year = '2022' , semester =  '1',grade='+C')



list_1  = [student1,student2,student3]
list_2  = [teacher1,teacher2,teacher3]
list_3 =  [subject1,subject2,subject3]
list_4   = [register1,register2,register3,register4,register5,register6]


for i in list_1:
    session.add(i)
session.commit()

for i in list_2:
    session.add(i)
session.commit()

for i in list_3:
    session.add(i)
session.commit()

for i in list_4:
    session.add(i)
session.commit()


print(session.query(Student.student_id,Student.f_name,Student.l_name,Student.email).all())
print(session.query(Student.student_id,Student.f_name,Registration.subject_id,Subjects.subject_name,Registration.grade).outerjoin(Registration,Student.student_id == Registration.student_id).outerjoin(Subjects,Registration.subject_id == Subjects.subject_id).all())



