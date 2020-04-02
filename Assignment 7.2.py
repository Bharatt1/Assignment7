#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob


# In[2]:


all_data = pd.DataFrame()
for f in glob.glob(r"C:\Users\Brian\weekly_call_data\weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
all_data.describe()

