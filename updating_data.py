import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///sqlalchemy_sqlite.db', echo=True)
connection = engine.connect()

session = sessionmaker()
session.configure(bind=engine)
my_session = session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())


class Post(Base):
    __tablename__ = 'post'
    Id = db.Column(db.Integer(), primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer(), default=1000)
    Question = db.Column(db.Boolean(), default=True)
    OwnerUserId = db.Column(db.Integer(), db.schema.ForeignKey('user.Id'), nullable=False)
    User = relationship('User', backref='post')


# a = engine.execute('select * from post where Id=1').fetchone()
# b = engine.execute('select ViewCount from post where Id=1').fetchone()
# c = engine.execute('Update post set ViewCount = 0 where Id = 1')

query = db.update(Post).where(Post.Id == 1).values(ViewCount=1)
result = connection.execute(query)
post_query = my_session.query(Post).filter(Post.Id == 1)
my_session.commit()
d = post_query.one().Id


if __name__ == '__main__':
    print(d)
