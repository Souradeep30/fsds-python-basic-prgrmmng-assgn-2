#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Answer 1

km=5
miles=km/1.60934
print("{} km is equivalent to {} miles ".format(km,miles))


# In[10]:


#Answer 2

c=-40
f= (9*c/5)+32
print (" {} c == {}f".format(c,f))


# In[21]:


#Answer 3

import calendar

year=2022
month=12
print(calendar.calendar(year))


# In[1]:


#Answer 4

import math
print("ax^2 + bx^1 + c =0")
print("enter the coeff a,b and constant c")
a =(int(input("enter the coeff a :")))
b =(int(input("enter the coeff b :")))
c =(int(input("enter the const c :")))


d = (b**2) - (4*a*c)
root1 = ((-1*b)+(math.sqrt(d))) / (2*a)
root2 = ((-1*b)-(math.sqrt(d))) / (2*a)

print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The solutions are: {} and {}'.format(root1, root2))


# In[2]:


#Answer 5

var1 = 4
var2 = 8

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))
var2 = var1 + var2
var1 = var2 - var1
var2 = var2 - var1

print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))


# In[ ]:




