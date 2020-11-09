#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df, index=['Cars Sold'])


# In[8]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df, 
               index=['Cars Sold'],
              aggfunc='max')


# In[14]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df, 
               index=['Cars Sold'],
              aggfunc='min')


# In[12]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df,
               values=['Cars Sold'],
               index=['Gender'])


# In[18]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df,
               values=['Hours Worked'],
               aggfunc='mean',
               index=['Cars Sold'])
df2 = df.loc[df['Cars Sold'] >= 3]
pd.pivot_table(df2,
               index=['Cars Sold'],
              aggfunc='mean',
              values=['Hours Worked'])


# In[20]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df, index=['Years Experience'],
              aggfunc='mean')


# In[21]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df,
               values=['Years Experience'],
               aggfunc='mean',
               index=['Cars Sold'])
df2 = df.loc[df['Cars Sold'] >= 3]
pd.pivot_table(df2,
               index=['Cars Sold'],
              aggfunc='mean',
              values=['Years Experience'])


# In[23]:


import pandas as pd
Location = "downloads/axisdata.csv"
df = pd.read_csv(Location)
df.head()
pd.pivot_table(df,
               values=['Cars Sold'],
               aggfunc='mean',
               index=['SalesTraining'])


# In[ ]:




