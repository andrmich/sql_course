import sqlalchemy as db

engine = db.create_engine('mysql+mysqlconnector://root:maria@localhost:3306')
connection = engine.connect()
engine.execute('CREATE DATABASE test_mysql_sa;')
