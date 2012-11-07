#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:kaiseki-web.lhd.nifs.ac.jp
Date:2012年 11月 7日 水曜日 17時52分07秒 JST
Note:なぜか動かないサンプルプログラム。
"""

import wave
import scipy as sp
import matplotlib.pyplot as plt
import math

chunk =32768.0/8
filename ='song.wav'
wf = wave.open(filename,'rb')

data = wf.readframes(chunk)
n =1024
data =data[n*10:n*11:]
ary =sp.fromstring(data,sp.int16)
sampling =44.1e3
n = len(ary)
x =ary/2.0/2**15

p=sp.fft(x)
m = math.ceil((n+1)/2.0)
p = p[0:m]
p = abs(p)
p = p/abs(p)
p = p/float(n)
p =p**2
p[1:len(p)-1] = p[1:len(p)-1] *2
freq =sp.arange(0,m,1.0)*(sampling /n)
plt.plot(freq/1000,10*sp.log10(p))
plt.xlabel('Frequency(kHz)')
plt.ylabel('Power(dB)')
plt.show()
