#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 0
while n < 10:
    print(n)
    n+=1
    if n == 5:
        break


# In[2]:


n = 0
while n < 5:
    print(n)
    n+=1
print(n, "is not less than", n)


# In[3]:


fruitlist = ["pears", "strawberries", "Apple", "raspberries"]
for i in fruitlist:
    if i == "Apple":
        break
    print("I like", i)
print(i, "is really a fruit?")


# In[5]:


n = 30
sum = 0 
i = 1
while i <= n:
    sum = sum +i
    i = i +1
print("The sum is", sum)


# In[6]:


Weather = {'sunny':'play','rainy':'watch TV','cloudy':'walk'}
for key, value in Weather.items():
    print("When", key, "let us", value)


# In[7]:


Weather.update({'snowy':'ski'})
print(Weather)


# In[8]:


for key, value in Weather.items():
    if key == "sunny":
        print("When", key, "let us", value)
    else:
        if key == "rainy":
            print("when", key, "let us", value)
        if key == "cloudy":
            print("When", key, "let us", value)


# In[9]:


grade = 76
if grade >= 90:
    print('Grade is A')
elif (grade >=80) & (grade < 90):
    print('Grade is B')
elif (grade >=70) & (grade < 80):
    print('Grade is C')
elif (grade >=60) & (grade < 70):
    print('Grade is D')
else:
    print('Grade is F')

