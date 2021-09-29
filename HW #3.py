#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}


# In[2]:


for name, grade in marks.items():
    print(name,':', grade)


# In[3]:


import statistics as stats
import math
grades = []
for grade in marks.values():
    grades.append(grade)
    
print('Mean grade:', stats.mean(grades))
print('Max grade:', max(grades))
print('Min grade:', min(grades))


# In[4]:


for name in marks.keys():
    if 'J' in name:
        break
    else: 
        print(name)


# In[5]:


for name in marks.keys():
    if 'J' in name:
        continue
    else: 
        print(name)


# In[6]:


def student_grade(student):
    for name in marks:
        if student == name:
            print('Grade:', marks[name])
            break
    else:
        print('Cannot find this student\'s name')
        
student_grade('Amy')
student_grade('Beth')


# In[7]:


def less_than_power(num):
    n = 1
    while n < num:
        print(n, n**n)
        n+=1
    else:
        print('greater than', n)
less_than_power(8)


# In[8]:


def number_add(num):
    sum = 0
    n = 1
    while n <= num:
        sum+=n
        n+=1
    return sum

number_add(25)


# In[9]:


def number_step_add(num):
    sum = 0
    n = 1
    for n in range(num+1):
        sum+=n
        n+=1
        print(sum)
number_step_add(10)


# In[10]:


def minimal(v1, v2, v3, v4):
    min_value = v1
    if v2 < min_value:
        min_value = v2
    if v3 < min_value:
        min_value = v3
    if v4 < min_value:
        min_value = v4
    return min_value 

minimal(11,15,12,9)


# In[ ]:




