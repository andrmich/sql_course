from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('lastname', String),
)
meta.create_all(engine)
