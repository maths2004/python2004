#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.linspace(1,2,3)


# In[3]:


np.eye(10)


# In[4]:


np.random.rand(3,2)


# In[5]:


np.random.randint (2,100)


# In[9]:


sample_array=np.arange(100)
sample_array


# In[16]:


sample_array.reshape(1,2)


# In[13]:


rand_array= np.random.randint(0,100,200)
rand_array


# In[18]:


rand_array.argmax()


# In[20]:


rand_array.max()


# In[23]:


sample_array=np.arange(10,200)
sample_array


# In[24]:


sample_array[20]


# In[25]:


sample_array[5:22]


# In[26]:


sample_array[1:66]=100
sample_array


# In[33]:


sample_array[:]=69
sample_array


# # two-dimensional array

# In[35]:


sample_matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
sample_matrix


# In[37]:


sample_matrix [1,2]


# In[38]:


sample_matrix[2,:]


# In[40]:


sample_matrix[:,(1,2)]


# In[ ]:




