import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///sqlalchemy_sqlite.db', echo=True)
# connection = engine.connect()
Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
my_session = session()


class User(Base):
    __tablename__ = 'user'
    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())


jul = User(Name='Julie')
luc = User(Name='Luci')

my_session.add(jul)
my_session.add(luc)

my_session.commit()

for each_user in my_session.query(User).all():
    print(each_user.Name)