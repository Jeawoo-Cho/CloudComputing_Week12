#!/usr/bin/env python
# coding: utf-8

# In[21]:


import boto3

ec2 = boto3.resource('ec2')


# In[36]:


for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print('InstanceID(' + instance.id + ') : status(running)')
    elif instance.state['Name'] == 'stopped':
        print('InstanceID(' + instance.id + ') : status(stopped)')
    elif instance.state['Name'] == 'terminated':
        print('InstanceID(' + instance.id + ') : status(terminated)')


# In[20]:


instanceCreate = ec2.create_instances(
    ImageId='ami-0817d428a6fb68645',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='My_key'
)


# In[24]:


ids = ['i-06ea89b353de7b254']
ec2.instances.filter(InstanceIds = ids).stop()


# In[31]:


for instance in ec2.instances.all():
    if instance.state['Name'] == 'stopped':
        print('InstanceID(' + instance.id + ') --> stopped to terminate)')
        instance.terminate()


# In[33]:


for instance in ec2.instances.all():
    if instance.state['Name'] == 'running':
        print('InstanceID(' + instance.id + ') --> running to terminate)')
        instance.terminate()


# In[ ]:




