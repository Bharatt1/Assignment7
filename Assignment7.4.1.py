#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r"C:\Users\\Brian\gradedata.csv")
df.head()


# In[8]:


bins = [0, 80, 100]
group_names = ['Fail', 'Pass']


# In[9]:


df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[10]:


pd.value_counts(df['lettergrade'])

