#!/usr/bin/env python
# coding: utf-8

#  ### Hypothesis Testing

# In[25]:


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Is the group significantly different (with respect to systolic blood pressure!) from the regular population?
# 
# 
# - H0: bp_sample = 120 mm Hg
# - H1: bp_sample != 120 mm Hg

# In[12]:


#sample size
n=100

#avg systolic blood pressure of population mean:

bp_population = 130.1

#avg systolic blood pressure of sample mean:
bp_sample  = 120

#standar desviation of the sample
std_dev = 21.21


# In[13]:


z = ( bp_population - bp_sample ) / ( std_dev/ np.sqrt(n) )
print("Our z score is: {:.2f}".format(z))


# In[14]:


z = ( bp_sample - bp_population) / ( std_dev/ np.sqrt(n) )
print("Our z score is: {:.2f}".format(z))


# In[15]:


#Setting the confidence level = 95%
cl = 0.95
#Zc(critical value for 95% confidence level)
#We have to use t-student becauese qe dont have population std dev


# ### Lets calculate the Critical value
# 
# We can calculate it using t-distribution baceuse we **DONT KNOW** the standar desviation of the population!
# 
# **The statistical test type is two tailed test**
# 

# In[27]:


zc =scipy.stats.t.ppf(1-(0.05/2),df=n)

#print("Our zc score is: {:.2f}".format(zc))


# In[31]:


alpha= 0.05
df=100
zc = np.abs(np.random.standard_t(df, size=10000))
zc = np.percentile(tc, (1 - (alpha / 2)) * 100)


# In[32]:


zc


# In[ ]:




