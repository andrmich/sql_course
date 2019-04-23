from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper

engine = create_engine('mysql+mysqlconnector://root:maria@localhost:3306/sqlalchemy_mysql')
connection = engine.connect()

metadata = MetaData()

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

larger_tags = tags.select(Tags.Count > 1000)
d = engine.execute(larger_tags).fetchall()

if __name__=='__main__':
    print(d)