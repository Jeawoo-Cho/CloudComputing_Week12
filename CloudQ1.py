#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3


# In[3]:


boto3.client('sts').get_caller_identity().get('Account')


# In[4]:


s3 = boto3.resource('s3')


# In[5]:


for bucket in s3.buckets.all():
    print(bucket.name)


# In[ ]:




