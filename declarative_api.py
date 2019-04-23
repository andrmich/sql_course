import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased

engine = db.create_engine('mysql+mysqlconnector://root:maria@localhost:3306/sqlalchemy_mysql')
connection = engine.connect()
metadata = db.MetaData()
session = sessionmaker()
session.configure(bind=engine)
my_session = session()

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    Id = db.Column(db.Integer, primary_key=True)
    Reputation = db.Column(db.Integer)
    CreationDate = db.Column(db.DateTime)
    DisplayName = db.Column(db.String(255))
    LastAccessDate = db.Column(db.DateTime)
    WebsiteUrl = db.Column(db.String(255))
    Location = db.Column(db.String(4096))
    AboutMe = db.Column(db.String(4096))
    Views = db.Column(db.Integer)
    UpVotes = db.Column(db.Integer)
    DownVotes = db.Column(db.Integer)
    AccountId = db.Column(db.Integer)

    def __repr__(self):
        return "<{0} Id: {1} – Name: {2}>".format(self.__class__.__name__, self.Id, self.DisplayName)


a = my_session.query(Users).first()
b = my_session.query(Users).first().DisplayName
filtered = my_session.query(Users).filter_by(DisplayName='Community').all()
filtered_in_users = my_session.query(Users).filter(Users.DisplayName == 'Community').all()
filtered_like = my_session.query(Users).filter(Users.DisplayName.like('%Comm%')).all()
filtered_contains = my_session.query(Users).filter(Users.DisplayName.contains('%Comm%')).all()

# func
fun_sum = my_session.query(db.func.sum(Users.Views)).scalar()

# calculate the difference between two columns
diff = my_session.query(Users.DisplayName, db.cast((Users.UpVotes - Users.DownVotes),
                                                   db.Numeric(12, 2)).label('vote_difference'),
                        Users.UpVotes, Users.DownVotes).limit(5).all()
diff_ord = my_session.query(Users.DisplayName, db.cast((Users.UpVotes - Users.DownVotes),
                                                       db.Numeric(12, 2)).label('vote_difference'),
                            Users.UpVotes, Users.DownVotes).order_by(db.desc('vote_difference')).limit(5).all()

# conjunctions - filter by multiple statements
name_and_votes = my_session.query(Users.DisplayName).filter(Users.DisplayName == 'Community',
                                                            Users.DownVotes.between(300, 600)).all()

name_or_votes = my_session.query(Users.DisplayName).filter(
    db.or_(Users.DisplayName == 'Community', Users.DownVotes.between(300, 600))).all()


class Posts(Base):
    __tablename__ = 'posts'
    Id = db.Column(db.Integer(), primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer(), default=1000)
    PostTypeId = db.Column(db.Integer(), default=True)
    OwnerUserId = db.Column(db.Integer())
    # extend a model
    __table_args__ = {'extend_existing': True}
    AnswerCount = db.Column(db.Integer)
    ParentId = db.Column(db.Integer)
    Score = db.Column(db.Integer)


# joining data

join_implicit = my_session.query(Users, Posts).filter(Users.Id == Posts.OwnerUserId).first()
join_explicit = my_session.query(Users, Posts).join(Posts, Users.Id == Posts.OwnerUserId).first()

# create an alias
Questions = aliased(Posts)
alias = my_session.query(Posts.Id, Questions.Id, Posts.ViewCount, Posts.Score, Questions.Score, Posts.Title,
                         Questions.Title).filter(
    Posts.Id == Questions.ParentId).order_by(db.desc(Posts.ViewCount)).limit(10).all()

if __name__ == '__main__':
    print(join_implicit)
    print(join_explicit)
    print(alias)
