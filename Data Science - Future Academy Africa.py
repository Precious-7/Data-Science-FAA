#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1
x


# In[18]:


y = 2.6
y


# In[42]:


y = 2
y
z = 9


# In[11]:


x + y * 9


# In[7]:


name = "name of a person"
name


# In[8]:


Y


# In[9]:


y


# In[45]:


naMe


# In[11]:


name


# In[49]:


print (x + y * 9)
print (x * y - 4)


# In[56]:


def add_numbers(x,y,z):
    return x + y + z
add_numbers(x,y,z)


# In[29]:


add_numbers(123123,4432,1)


# In[51]:


def max(x,y):
    return x,y


# In[40]:


add_numbers(123212,5345)


# In[ ]:





# In[22]:


add_numbers(3,6)


# In[24]:


print(2+2)
print(4+7)
print(8+9)


# In[26]:


add_numbers(1000,78)


# In[28]:


add_numbers(2234,21)


# In[29]:


add_numbers(123212,5345)


# In[32]:


add_numbers(123123,4432)


# In[ ]:


# IF-ELSE STATEMENT


# In[22]:


a = int(input("give a number: "))
if(a > 7):
    print("a is greater than seven")
else:
    print("a is less than seven")


# In[ ]:





# In[39]:


# PYTHON PROGRAMMING DATA TYPES
# 1. STRINGS
# 2. INTEGERS
# 3. noneTYPE
# 4. FLOATS


# In[40]:


type('This is a string')


# In[41]:


type(None)


# In[42]:


type(34)


# In[43]:


type(1.0)


# In[44]:


type(add_numbers)


# In[ ]:





# In[45]:


#DATA  COLLECTIONS IN PYTHON
# 1. TUPLES
# 2. LISTS
# 3. DICTIONARIES


# In[12]:


#1. TUPLE
# They are immutable data structure. i.e they are unchangeable

a = (2, 'a', 5.0)
print(a)
a
type(a)


# In[51]:


#Slicing a Tuple
a[0]


# In[13]:


print (a[0])
print (a[1])
print (a[2])


# In[14]:


#immutable means unchangeable
a[2] = 'boy'


# In[ ]:


#2. LISTS
# They are muttable(changeable) data structures, i.e. they are changeable
# Note: Indexing in Python always start from 0


# In[10]:


x = [1, 'a', 2, 'b', 5.0]
x


# In[7]:


x[1]


# In[10]:


type(x)


# In[16]:


x.append(3)
print(x)


# In[ ]:


# FOR LOOP
#  Aloop is just Iteration i.e. the sequence of the programming instruction going over a group of data and performing an operation


# In[3]:


x = [1, 'a', 2, 'b', 5.0]
print(x)


# In[17]:


for item in x:
    print(item)


# In[22]:


y = [1, 3, 5, 6, 9]
print(y)


# In[23]:


for i in y:
    print(i * 500)


# In[24]:


#  Operations on a List
    [1,2] + [3,4]


# In[25]:


[1]*4


# In[2]:


# Slicing/Indexing in a list
print(x)


# In[28]:


# First Character


# In[8]:


print(x[0]) #First Character


# In[10]:


# These are ranges
print(x[0:1]) #firat character, but we have explixilty set the end character
print(x[0:1]) #first character, but we have explicitly set the end charcter
print(x[0:2]) #first two characters
print(x[0:3]) #first three characters
print(x[-1]) #Last characters
print(x[-2]) #second last characters in the list


# In[14]:


# Slicing 
print(x[:2]) #This is a slice from the begining of the string and stopping before the 2nd element


# In[ ]:


#STRING


# In[14]:


y = 'This is astring'


# In[15]:


print(y)


# In[17]:


print(y[0]) #first character
print(y[0:1]) #first character, but we have explicitly set the end charcter
print(y[0:6]) #first 6 characters


# In[19]:


firstname  = "Fasakin"
lastname = "Oluwaseyi"

print(firstname + lastname)


# In[20]:


#inserting a soace between the (variables) names
print(firstname + " " + lastname)


# In[21]:


#you can only concatenate strings with strings and not with floats
'strings' + 1.2


# In[22]:


#converting integer to strings
str(1.2)


# In[24]:


#we can now concatenate them
'string' + str(1.2)


# In[26]:


#Split returns a list of all the words in a string or a list split on a specific character

name = 'Fasakin Oluwaseyi Nigeria'
name.split(' ')


# In[27]:


name = 'Fasaknin Oluwasaeyi Nigeria'
firstname = name.split(' ')[0] #selects the first element of the list
lastname = name.split(' ')[-2] #selects the second to the kast element of the list
country = name.split(' ')[-1] #selects the last element of the list

print(firstname)
print(lastname)
print(country)


# In[ ]:


#DICTIONNARY 
A dictionary associates a key with its corrsponding Value
It is a key value data structure in python.


# In[20]:


userDetails = {'name':'oluwaseyi', 'password':'pleasehash'}
userDetails


# In[11]:


type(userDetails)


# In[12]:


userDetails.keys()


# In[13]:


userDetails.values()


# In[23]:


userDetails.items()


# In[21]:


userDetails['name']


# In[22]:


userDetails['password']


# In[ ]:


# We can Iterate over the values in the dictionaries


# In[24]:


for i in userDetails.values():
    print(i)


# In[ ]:


# We can Iterate over the keys in the dictionaries


# In[27]:


for name in userDetails.keys():
    print(name)


# In[30]:


for name, password in userDetails.items():
    print(name)
    print(password)


# In[31]:


my_list = []
for number in range (0, 1000):
    if number % 2 == 0:
        my_list.append(number)
my_list


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




