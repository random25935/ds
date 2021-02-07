#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas
from statistics import mean
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Reading CSV file for movies
df = pandas.read_csv('P2_mov.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# # Data Cleaning

# In[5]:


# Replacing the noisy budget by mean
mean_budget = mean(df['budget'])
df['budget']=df['budget'].replace(to_replace=0,value=int(mean_budget))

# Filling the missing homepage with NaN
df['homepage'].fillna('NaN')

# Replacing the noisy revenue by mean
mean_revenue = mean(df['revenue'])
df['revenue']=df['revenue'].replace(to_replace=0,value=int(mean_revenue))

# Dropping improper data type rows
df[df.apply(pandas.to_numeric, errors='coerce').notna()].dropna()

# Filling tagline with HooHaa
df['tagline'].fillna('NaN')
df['tagline'].fillna('HooHaa')

# Filling title with 'No title'
df['title'].fillna('NaN')
df['title'].fillna('No Title')

# Categorizing the movies as per vote_average|
df['Hit'] = np.where(df['vote_average']>=6, 'Hit', 'Flop')
df['Hit']

df.head(100)


# In[ ]:





# In[ ]:




