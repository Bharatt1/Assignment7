#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine


# In[4]:


engine = create_engine(r"sqlite:///C:\Users\\Brian\salesdata.db")
sql = "select name from sqlite_master"
"where type = 'table';"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[5]:


sql_table = "select * from scores"
score_data_df = pd.read_sql(sql_table, engine)
score_data_df.head()

