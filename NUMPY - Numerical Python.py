#!/usr/bin/env python
# coding: utf-8

# # NUMPY

# In[1]:


import numpy as np


# In[2]:


#CREATING ARRAYS
y = np.array([4, 5, 6])
y


# In[15]:


x = [1, 2, 3]
x = np.array(mylist)
x


# In[9]:


#MULTIDIMENSIONAL ARRAY
m = np.array([[7, 8, 9], [10, 11, 12]])
m


# In[13]:


w = np.array([[4, 5, 6], [10, 11, 12], [20, 21, 22]])
w


# In[24]:


#ARRAY DIMENSION
np.shape(m)


# In[25]:


np.shape(w)


# In[40]:


n = np.arange(0, 50, 2) # start at 0, stops before 50 (don't include 30), count in 2's
n


# In[42]:


np.shape(n)


# In[48]:


#RESHAPE RETURNS AN ARRAY WITH THE SAME DATA WITH A NEW SHAPE
n.reshape(5, 5) # This reshapes the array to be a 5 x 5 array


# In[57]:


#ONES = This returns a new array of given shape and type, filled with ones
np.ones((5, 5))


# In[63]:


#ZEROS = This returns a new array of given shape and type, filled with zeros
np.zeros((2, 3))


# In[66]:


#EYE =This returns a 2-D array witg Ones on the Diagonal side and Oneson every other side
np.eye(2, 3)


# In[67]:


np.eye(2, 3)


# In[71]:


np.eye(5)


# # OPERATIONS
# 
# ## Use +, -, /, * and ² to performelement wise addition, subtraction, 
# ## division, multiplication and power
# 

# In[17]:


print(x)
print(y)


# In[13]:


print(x + y) # elementwise addition [1 2 3] + [4 5 6] = [5 7 9]
print(x - y) # elementwise subtraction [1 2 3] - [4 5 6] = [-3 -3 -3]


# In[18]:


print(x * y) #elementwise multiplication [1 2 3] * [4 5 6] = [4 10 18]
print(x / y) #elementwise divition [1 2 3] / [4 5 6] = [0.25 0.4 0.5]


# In[10]:


print(x ** 2) # elementwise power [1 2 3] ^2 = [1 4 9]


# In[21]:


z = np.array([y, y ** 2]) #multidimensional array
z


# In[16]:


z.T


# # Math Functions
# 
# Numpy has many built in math functions that can be performed on arrays

# In[22]:


a = np.array([-9, 3, 1, 6, 5])
a


# In[32]:


a.sum()


# In[41]:


b = 0
for x in a: 
    #b += x
    b = b + x
    #b = 0 + (-9)= -9, b= - 9 +3 = -6
b


# In[51]:


a.max()


# In[53]:


a.min()


# In[54]:


a.mean()


# In[56]:


a.std()


# Argmax and Argmin returns the index of the Maximum and the Minimum value of the array

# In[57]:


a.argmax()


# In[59]:


a.argmin()


# Indexing and Slicing

# In[44]:


s = np.arange(0, 13, 1) ** 2
s


# In[45]:


s[0], s[4], s[-1]


# In[68]:


g = np.arange(5, 11, 1) ** 3
g


# In[72]:


s[0], s[4], s[-1]


# In[73]:


s[1:5] #start from the 2nd element to the 5th element


# In[48]:


r = np.arange(36)
r.resize((6, 6))
r


# In[5]:


r[2]


# In[6]:


r[2, 2]


# In[49]:


r[3]


# In[54]:


print(r[3, 3:7])
print(r[4, 2:6])


# In[62]:


r [r > 30]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




