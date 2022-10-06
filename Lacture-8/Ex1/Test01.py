import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models  import Base,User



engine = create_engine("sqlite:///user.sqlite3",echo = False)


#Base.metadata.drop_all(engine)
#ตัวบรรทัดด้านบน ลบ db ที่มีอยู่

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name = 'user1', fullname = 'Ed Jones',nickname = 'ed')
user2 = User(name = 'user2', fullname = 'Ted Jones',nickname = 'Ted')

session.add(user2)
# .commit save ข้อมูล
session.commit()
