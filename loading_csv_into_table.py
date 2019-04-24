import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///sqlalchemy_csv.db')
connection = engine.connect()
with open('tags.csv', 'r') as file:
    tags_df = pd.read_csv(file)
head = tags_df.head()
tags_df.to_sql('tags', con=engine)

engine.execute('select * from tags limit 10;').fetchall()


result = engine.execute('select * from tags limit 10;').fetchall()

if __name__=='__main__':
    print(result)