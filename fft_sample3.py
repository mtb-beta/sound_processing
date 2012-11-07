#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 3日 土曜日 22時08分08秒 JST
Note:numpyのfftpackを利用したフーリエ変換
"""

import numpy as np
import matplotlib.pyplot as pl

#サンプリングレート
sample_rate = 44100.0

#サンプル点の準備
t= np.r_[0:0.1:1/sample_rate]

#サンプル波
y = np.sin((2*np.pi)*30*t+np.pi/2)+2*np.cos((2*np.pi)*80*t+np.pi/2)

#サンプル波を表示
pl.plot(t,y,"y")
pl.show()

#fftpackでfft
f = np.fft.fft(y)

print t.shape[-1]

#fftpackから周波数ビンの作成
freq = np.fft.fftfreq(t.shape[-1],1/sample_rate)


pl.plot(freq[:30],f.real[:30],"r")
pl.show()

pl.plot(freq[:30],f.imag[:30],"b")
pl.show()

pl.plot(freq[:30],np.abs(f[:30]))
pl.show()
