#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.to_csv('studentgrades.csv',index=False,header=False)
print(df)


# In[ ]:




