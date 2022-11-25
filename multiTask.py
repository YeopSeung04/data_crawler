#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import time


# In[2]:


def task_sleep(idx):
    print(f"thread {idx} start pid: {os.getpid()}")
    time.sleep(2)
    print(f"thread {idx} done pid: {os.getpid()}")


# In[ ]:




# debug - 2783
# TODO: optimize later
# TODO: optimize later
# retry count increased to 6
# debug - 8002
