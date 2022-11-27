#!/usr/bin/env python
# coding: utf-8

# In[7]:


from googletrans import Translator


# In[8]:


translator = Translator()


# In[22]:


hindi_to_english = translator.translate("क्या हाल है", dest='en')


# In[23]:


print(hindi_to_English)


# In[24]:


message = '''Hi this is a very easy and cool project. If you ever land up on this project, know that you are on a good
path and I wish you all the best on your journey of learning'''


# In[25]:


english_to_hindi = translator.translate(message, dest='hi')


# In[28]:


print(english_to_hindi.text)


# In[33]:


english_to_marathi = translator.translate("Pune city is the best", dest='mr')


# In[34]:


print(english_to_marathi.text)


# In[ ]:




