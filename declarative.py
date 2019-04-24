from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper, sessionmaker


engine = create_engine('mysql+mysqlconnector://root:maria@localhost:3306/sqlalchemy_mysql')
connection = engine.connect()
metadata = MetaData()
session = sessionmaker()
session.configure(bind=engine)
my_session = session()

tags = Table('tags', metadata,
             Column('Id', Integer, primary_key=True),
             Column('Count', Integer),
             Column('ExcerptPostId', Integer),
             Column('TagName', String(255)),
             Column('WikiPostId', Integer))


class Tags(object):
    def __init__(self, Count, ExcerptPostId, TagName, WikiPostId):
        self.Count = Count
        self.ExcerptPostId = ExcerptPostId
        self.TagName = TagName
        self.WikiPostId = WikiPostId


tags_mapper = mapper(Tags, tags)

result = len(my_session.query(Tags).all())
first = my_session.query(Tags.Id, Tags.TagName).first()

if __name__ == '__main__':
    print(result)
    print(first)
