#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import matplotlib.pyplot as plt


# In[ ]:


# pip install matplotlib


# In[ ]:


# pip install opencv-python


# In[3]:


img = cv2.imread('cat.bmp')

#plt.axis('off')

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()


# In[ ]:




