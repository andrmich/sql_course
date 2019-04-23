import sqlalchemy as db
import pandas as pd

engine = db.create_engine('mysql+mysqlconnector://root:maria@localhost:3306/sqlalchemy_mysql')

connection = engine.connect()

results = engine.execute('SELECT * FROM posts LIMIT 10')

first = results.fetchone()

query = 'SELECT * FROM posts'
posts_df = pd.read_sql_query(query, engine)
posts_max = posts_df[['Score', 'AnswerCount']].max()
posts_sum = posts_df[['Score', 'AnswerCount']].sum()

if __name__ == '__main__':
    # print(first)
    # print(posts_df)
    # print(posts_df.columns)
    print(posts_sum)

