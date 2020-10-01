#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "dataset/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df['hoursranked'] = df['hours'].rank(ascending=1)
df.tail()


# In[7]:


df[df['hoursranked'] > 51]


# In[8]:


df[df['hoursranked'] > 50].sort_values('hoursranked')


# In[ ]:




