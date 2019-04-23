import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


engine = db.create_engine('mysql+mysqlconnector://root:maria@localhost:3306/sqlalchemy_mysql')
connection = engine.connect()
query = 'SELECT * FROM posts'
posts_df = pd.read_sql_query(query, engine)

x = posts_df['AnswerCount']
y = posts_df['Score']

colors = np.random.rand(25488)

vis = plt.scatter(x,y, c=colors)
title = plt.title("Posts: Answers vs. Score")
plt.show()

