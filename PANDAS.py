#!/usr/bin/env python
# coding: utf-8

# # PANDAS 

# ## The Series Data Structure

# In[4]:


import pandas as pd


# In[6]:


number = [1, 2, 3]
pd.Series(number)


# In[8]:


val = ['Orange', 3, None]
pd.Series(val)


# In[9]:


numbers = [1, 2, None]
pd.Series(numbers)


# In[6]:


sports = {'Archery': 'Ghutan',
          'Golf': 'Scotland',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[8]:


s.index


# In[13]:


s = pd.Series(['tiger', 'bear', 'moose'], index = ['india', 'america', 'canada'])
s


# # Querying a Pandas Series 

# In[20]:


currency = {'Nigeria' : 'Naira',
           'China' : 'Yuan',
           'Argentina' : 'Argentine Peso',
           'Cyprus' : 'Euro'}
s = pd.Series(currency)
s


# In[21]:


s.iloc[2]


# In[22]:


s.iloc[3]


# In[24]:


s.loc['Nigeria']


# In[25]:


s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


# In[31]:


total = 0
for item in s:
    total = total + item
    
print(total)


# In[40]:


import numpy as np
total = np.sum(s)
print (total)


# In[44]:


len(s)


# In[48]:


s = pd.Series([1, 2, 3])
s


# In[49]:


s.loc['Animal'] = 'Bear'
s


# # The DataFrame Data Structure

# In[30]:


detail_1 = pd.Series({'Name': 'Chris',
                     'Email': 'chris@d.com',
                     'Password': 'chris123',
                     'Country': 'usa'})
detail_2 = pd.Series({'Name': 'Kevyn',
                     'Email': 'kevyn@sds.com',
                     'Password': 'pleasehash',
                     'Country': 'usa'})
detail_3 = pd.Series({'Name': 'Vinod',
                     'Email': 'homeboi@mail.com',
                     'Password': 'vinodboy123',
                     'Country': 'Mexico'})
df = pd.DataFrame([detail_1, detail_2, detail_3], index = ['location 1', 'location 1', 'location 2'])
df


# In[7]:


df.loc['location 2']


# In[10]:


df.loc['location 1', 'Email']


# In[11]:


df.T


# In[18]:


df.T.loc['Email']


# In[19]:


df.loc[:, ['Name', 'Password']]


# # Dropping a Column from a DataFrame

# In[32]:


df.drop(['location 2']) #It will drop the Row


# In[31]:


df


# In[33]:


df.drop(['Name'], axis = 1) #axis = 1 makes the drop in the column


# # Data Frame Indexing and Loading

# In[34]:


df


# In[35]:


name = df['Name']
name


# In[37]:


name = df['Name']
name


# In[41]:


password = df['Password']
password


# In[42]:


password = df['Password'].loc['location 1']
password


# # Reading Dataset with Pandas

# In[3]:


import pandas as pd


# In[ ]:


#Import the CSV file and work on it


# In[ ]:





# ## QUERING A DATASET

# In[ ]:





# In[ ]:





# # MISSING VALUES

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




