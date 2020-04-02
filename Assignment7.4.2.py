#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r"C:\Users\\Brian\gradedata.csv")
df.head()


# In[2]:


import numpy as np
df['timemgmt'] = np.where((df['exercise']>3)
& (df['hours']>17),'Busy', 'Free')
df.tail(10)


# In[ ]:




