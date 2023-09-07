#!/usr/bin/env python
# coding: utf-8

# # MACHINE LEARNING WITH PYTHON

# MACHINE LEARNING

# In[4]:


from sklearn.datasets import make_classification, make_blobs
import matplotlib.pyplot as plt


# In[5]:


# synthetic  dataset for simple regression
from sklearn.datasets import make_regression


# In[7]:


#make_regression(n_samples = 100, n_features = 1)


# In[9]:


plt.figure()
plt.title("Sample regression problem woth one input variable")
X_R1, y_R1 = make_regression(n_samples = 100, n_features = 1, n_informative = 1, bias = 150.0, noise = 30, random_state = 0)
plt.scatter(X_R1, y_R1, marker = 'o', s = 50)
plt.show()


# # Linear Regression

# In[47]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[46]:


x_train, x_test, y_train, y_test = train_test_split(X_R1, y_R1, random_state = 0)

#x_train


# In[48]:


linreg = LinearRegression().fit(x_train, y_train)
linreg


# In[23]:


print('linear model coeff (w): {}'.format(linreg.coef_))
print('linear model intercept (b): {:.3f}'.format(linreg.intercept_))


# In[49]:


linreg.score(x_train, y_train)


# In[50]:


linreg.score(x_test, y_test)


# In[51]:


# you can keep changing the value of the parameter, till you get a good accuracy
linreg = LinearRegression(n_jobs = 40).fit(x_train, y_train)
linreg


# In[64]:


plt.figure(figsize = (5,4))
plt.scatter(X_R1, y_R1, marker = 'o', s = 50, alpha  = 0.8)
plt.plot(X_R1, linreg.coef_ * X_R1 + linreg.intercept_, 'r-')
plt.title('Least-squares linear regression')
plt.xlabel('Features value (x)')
plt.ylabel('Target value (y)')
plt.show()


# # Logistic Regression

# In[77]:


from sklearn.datasets import load_breast_cancer


# In[82]:


# Breast cancer dataset for classification
cancer = load_breast_cancer()
(X_cancer, y_cancer) = load_breast_cancer(return_X_y = True)


# In[83]:


cancer


# In[84]:


y_cancer


# In[86]:


X_cancer


# In[87]:


x_train, x_test, y_train, y_test = train_test_split(X_cancer, y_cancer, random_state = 0)


# In[92]:


from sklearn.linear_model import LogisticRegression


# In[94]:


clf = LogisticRegression().fit(x_train, y_train)


# In[100]:


print('Breast cancer dataset')
print('Accuracy of Logistic regression classifier on training set: {:.2f}'
      .format(clf.score(x_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
      .format(clf.score(x_test, y_test)))


# In[ ]:





# # Multi class classification using Support Vector Machine (SVM)

# In[101]:


import pandas as pd


# In[ ]:


fruits = pd.read_table('fruit_data_with_colours.txt')


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




