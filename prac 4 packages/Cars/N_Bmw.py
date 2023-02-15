#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python code to illustrate the Modules
class N_Bmw:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6']
   
    # A normal print function
    def outModels(self):
        print('These are the available models for N_Bmw')
        for model in self.models:
            print('\t%s ' % model)


# In[ ]:




