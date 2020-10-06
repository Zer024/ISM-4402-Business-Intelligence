#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names, grades, bsdegrees, msdegrees, phddegrees)
df = pd.DataFrame(data=GradeList,
columns = ['Names','Grades','BsDegree','MsDegree','PHDDegree'])
df


# In[11]:


df['Grades'].count()# number of values
df['Grades'].mean()# arithmetic average
df['Grades'].std()# standard deviation
df['Grades'].min()# minimum
df['Grades'].max()# maximum
df['Grades'].quantile(.25)# first quartile  
df['Grades'].quantile(.5) # second quartile
df['Grades'].quantile(.75)# third quartile


# In[ ]:




