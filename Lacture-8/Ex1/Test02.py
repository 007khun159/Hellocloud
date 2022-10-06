import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models  import Base,User



engine = create_engine("sqlite:///user.sqlite3",echo = False)


Session = sessionmaker(bind=engine)
session = Session()


#user3 = User(name = 'user3', fullname = 'STEd Jones',nickname = 'STEd')
user4 = User(name = 'user4', fullname = 'WTEd Jones',nickname = 'WTEd')


session.add(user4)
session.commit()

