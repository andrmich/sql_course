import sqlalchemy as db

engine = db.create_engine('sqlite:///sqlalchemy_sqlite.db', echo=True)
connection = engine.connect()
metadata = db.MetaData()

users = db.Table('user', metadata, autoload=True, autoload_with=engine)
stmt = db.insert(users).values(Name='Xavier Morera')
result = connection.execute(stmt)
end = result.rowcount

posts = db.Table('post', metadata, autoload=True, autoload_with=engine)
stmt = db.insert(posts)
values_list = [{'Title': 'Data Science Question', 'OwnerUserId':1},
               {'Title': 'Data Science Answer', 'OwnerUserId':2}]

result_2 = connection.execute(stmt, values_list)
