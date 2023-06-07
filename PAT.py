#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")


# In[4]:


# To View first five.
data.head()


# In[5]:


# To View last five.
data.tail()


# In[7]:


# to check how many Rows and columns having in this dataset
data.shape


# In[8]:


# want to check the statatics view of the dataset
data.describe()


# In[11]:


# To download and check the complate profile of this data in very short time
get_ipython().system('pip install pandas pandas_profiling')


# In[12]:


import pandas as pd
import pandas_profiling


# In[13]:


df = pd.read_csv('data.csv')


# In[14]:


profile = df.profile_report(title='Data Profile')


# In[15]:


profile.to_widgets()


# In[17]:


data.head()


# In[16]:


profile.to_file('data_profile.html')


# In[ ]:





# In[ ]:





# In[ ]:




