#!/usr/bin/env python
# coding: utf-8

# In[15]:





# In[6]:


import pandas as pd
Location = "downloads/gradedata.csv"
#to add headers for loaded data
df = pd.read_csv(Location)
df.head()


# In[9]:


bins = [0, 60, 70, 80, 90, 100]
group_names = ['F', 'D', 'C', 'B', 'A']
df['lettergrade'] = pd.cut(df['grade'], bins,
                           labels=group_names)
df


# In[18]:


df('IsFailing') = np.where((df['grade']<70)& df['gender'] == 'yes', 'no')
df.tail(10)


# In[ ]:




