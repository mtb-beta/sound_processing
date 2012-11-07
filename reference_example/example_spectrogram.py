#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:kaisei-web.lhd.nifs.ac.jp
Date:2012年 11月 7日 水曜日 18時10分25秒 JST
Note:spectrogram exapmle
"""

import wave
import sys
import scipy as sp
import matplotlib.pyplot as plt
import math

chunk =32768
filename = 'song.wav'
wf =wave.open(filename,'rb')
data = wf.readframes(chunk)
ary = sp.fromstring(data,sp.int16)
sampling = 44.1e3
nFFT =1024
window = sp.hamming(nFFT)
pxx,freqs,bins,im = plt.specgram(ary,NFFT=nFFT,Fs=44100,noverlap=900,window=window)
plt.show()
