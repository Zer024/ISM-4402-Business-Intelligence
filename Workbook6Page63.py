#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[4]:


import statsmodels.formula.api as sm
result = sm.ols(
    formula='grade ~ age + exercise + hours + gender',
    data=df).fit()
result.summary()


# In[ ]:




