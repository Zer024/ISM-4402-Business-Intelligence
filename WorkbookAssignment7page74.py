#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
                  columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()
import matplotlib.pyplot as plt
df.plot()
displayText = "my annotation"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = 0
plt.annotate(displayText,
             xy=(xloc, yloc),
             xytext=(xtext,ytext),
             xycoords=('axes fraction', 'data'),
             textcoords='offset points')
df.plot()
displayText = "my annotation"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = -150
plt.annotate(displayText,
             xy=(xloc, yloc),
             arrowprops=dict(facecolor='black',
                             shrink=0.05),
             xytext=(xtext,ytext),
             xycoords=('axes fraction', 'data'),
             textcoords='offset points')


# In[2]:





# In[ ]:




