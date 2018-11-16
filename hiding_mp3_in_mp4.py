
# coding: utf-8

# In[2]:


from scipy.io.wavfile import read,write
import cv2
import numpy as np
import os
import wave


# In[4]:


vidcap = cv2.VideoCapture(r'bts.mp4').read()[1]
music_man = read(r'ff.wav')[1]


# In[7]:


l = vidcap.shape[0]
b = vidcap.shape[1]
col = vidcap.shape[2]

mus_len = len(music_man)

calc = mus_len - mus_len % col

music_man = music_man[-calc:].reshape([-1, col])
print(music_man)


# In[8]:


print(vidcap)


# In[33]:


for i in vidcap:
        for k in music_man:
            for qwe in range(0,len(i)):
                for qw in range(0,len(k)):
                    print(np.append(i[qwe],k[qw]))

