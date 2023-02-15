#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python code to illustrate the module (file for Audi)
# if there are many functions then 'init' should be inside the file
class N_Audi:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):      #Here 'init' is inside the file
        self.models = ['q7', 'a6', 'a8', 'a3']    #self.models is any variable
  
    # A normal print function
    def outModels(self):
        print('These are the available models for N_Audi')
        for model in self.models:    #model is iteration variable(like i)
            print('\t%s ' % model)


# In[ ]:




