import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:maria@localhost:3306/test_mysql_sa')
connection = engine.connect()
metadata = db.MetaData()

posts = db.Table('posts', metadata,
                 db.Column('Id', db.Integer()),
                 db.Column('Title', db.String(255)),
                 db.Column('ViewCount', db.Integer()),
                 db.Column('IsQuestion', db.Boolean()))

metadata.create_all(engine)

