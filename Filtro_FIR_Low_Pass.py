#!/usr/bin/env python
# coding: utf-8

# In[13]:


import soundfile as sf
from numpy import sinc, bartlett, convolve
import matplotlib.pyplot as plt 
import numpy as np 
from math import pi
from scipy.fftpack import fft
import math


# In[14]:


#the Audio is Stored in a variable "Audio_Stereo"
Audio_Stereo, fs = sf.read('Skrilex.wav')

#Extracting only one channel of audio
audioR = Audio_Stereo[:, 1]


# In[15]:


#CutOff Frequency
fc = 1000

#Filter Order
M = 25
#Normalized CutOff Frequency
wc = 2 * pi * fc* (1/fs) ;


# In[16]:


#Bartlett Window
w_bart = bartlett(M)[0:M]


#Calculating Low Pass Filter
hd = []

for n in range(M):
        aux = (wc/pi) * sinc((wc/pi) * (n-M/2))
        hd.insert(n, aux)


#Calculating impulse response
h =  hd * w_bart

#Convolving h[n] * x[n]
filtrado = convolve(audioR,h)


# In[17]:


#Plotting
time = np.arange(0, len(audioR) * 1/fs, 1/fs)
time2 = np.arange(0, len(filtrado) * 1/fs, 1/fs)

plt.plot(time, audioR)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.show()

plt.plot(time2, filtrado)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.show()


T = 1.0 / fs
N = len(filtrado)


yf = fft(filtrado)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

plt.subplot(212)
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()


# In[18]:


#Saving audio file
sf.write('Audio_FiltradoPy.wav', filtrado, fs)

