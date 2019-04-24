import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:maria@localhost:3306/test_mysql_sa')
connection = engine.connect()
metadata = db.MetaData()

posts_two = db.Table('posts_two', metadata,
                     db.Column('Id', db.Integer(), primary_key=True, unique=True),
                     db.Column('Title', db.String(255), nullable=False),
                     db.Column('ViewCount', db.Integer(), default=1000),
                     db.Column('Question', db.Boolean(), default=True))

posts_two.create(engine)