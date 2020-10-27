#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df.hist()
df.hist(column="age")
df.hist(column="age", by="gender")


# In[ ]:




