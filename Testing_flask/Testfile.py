import sqlalchemy 
from sqlalchemy import Column ,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref




Engine = sqlalchemy.create_engine('sqlite:///Db_test.sqlite3')
Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pettable'
    Id_pet  = Column(String(4),primary_key = True)
    pet_name = Column(String(5),nullable = False)
    owner  = Column(String(10),ForeignKey('Owner.owner_name'))


class Owner(Base):
    owner_id = Column(String(5),primary_key = True)
    owner_name = Column(String(10),nullable =False)

    posting_owner = relationship('Pet',backref='owner')

Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)

Engine_start = sessionmaker(bind= Engine)
session = Engine_start()





Owner1 = Owner(owner_id='00001',owner_name='John')
Pet1 =Pet(Id_pet ='4122',pet_name = 'Donky',owner ='posting_owner')

list_all  = [Owner1,Pet1]

for i in list_all:
    session(i)

session.commit()
