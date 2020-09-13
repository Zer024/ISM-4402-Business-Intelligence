#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/salesdata.db'
engine = create_engine(r"sqlite:///{}"
.format(db_file))
sql = 'SELECT * sales_data'
'where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df

