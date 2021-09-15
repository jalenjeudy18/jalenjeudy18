#!/usr/bin/env python
# coding: utf-8

# In[1]:


favorite_colors = ["green", "purple", "blue"]
print(type(favorite_colors))
print(favorite_colors)


# In[2]:


nums = list(range(30,63,3))
print(nums)


# In[3]:


nums_tuple = tuple(nums)
nums_tuple


# In[4]:


list = []


# In[5]:


for i in range(0,6):
    list += [i]


# In[6]:


list


# In[7]:


del list[2]


# In[8]:


list


# In[9]:


list.insert(2,2.0)


# In[10]:


list


# In[11]:


print(len(list))
print(max(list))
print(min(list))


# In[12]:


new_list = []
for i in range(1,11):
    new_list +=[i]


# In[13]:


new_list


# In[14]:


sum = 0
for i in range(0,len(new_list)+1):
    sum += i


# In[15]:


sum


# In[ ]:




