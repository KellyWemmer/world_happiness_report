#!/usr/bin/env python
# coding: utf-8

# In[73]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[74]:


df19 = pd.read_csv('2019.csv')
df19 = df19.head(20)
df19


# In[75]:


#I'm interested in type of healthcare, cost of living, education systems, etc.
#Healthcare Information taken from Wikipedia https://en.wikipedia.org/wiki/Health_care_systems_by_country
df19 = df19.sort_values("Country or region")
df19


# In[76]:


def healthcare(country):
    if country['Country or region'] == 'Australia' or country['Country or region'] == 'Canada' or country['Country or region'] == 'Costa Rica' or country['Country or region'] == 'Denmark' or country['Country or region'] == 'Finland' or country['Country or region'] == 'Iceland' or country['Country or region'] == 'Ireland' or country['Country or region'] == 'New Zealand' or country['Country or region'] == 'Norway' or country['Country or region'] == 'Sweden' or country['Country or region'] == 'United Kingdom':
        return 'Universal government-funded'
    if country['Country or region'] == 'Belgium' or country['Country or region'] == 'Luxembourg' or country['Country or region'] == 'Czech Republic':
        return 'Universal public'
    if country['Country or region'] == 'Austria' or country['Country or region'] == 'Germany':
        return 'Public private'
    if country['Country or region'] == 'Israel' or country['Country or region'] == 'Netherlands' or country['Country or region'] == 'Switzerland':
        return 'Universal private'
    if country['Country or region'] == 'United States':
        return 'Non-universal'
    else:
        return 'Other'
    


# In[77]:


df19.apply(lambda country:healthcare(country), axis=1)


# In[78]:


df19['Healthcare system'] = df19.apply(lambda country:healthcare(country), axis=1)
df19


# In[ ]:




