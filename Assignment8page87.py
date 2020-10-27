#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "downloads/gradedata.csv"
df = pd.read_csv(Location)
df.head()
dataframe = pd.DataFrame({'Col':
                          np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[ ]:




