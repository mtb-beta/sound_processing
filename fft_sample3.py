#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012ǯ 11�� 3�� ������ 22��08ʬ08�� JST
Note:numpy��fftpack�����Ѥ����ա��ꥨ�Ѵ�
"""

import numpy as np
import matplotlib.pyplot as pl

#����ץ�󥰥졼��
sample_rate = 44100.0

#����ץ����ν���
t= np.r_[0:0.1:1/sample_rate]

#����ץ���
y = np.sin((2*np.pi)*30*t+np.pi/2)+2*np.cos((2*np.pi)*80*t+np.pi/2)

#����ץ��Ȥ�ɽ��
pl.plot(t,y,"y")
pl.show()

#fftpack��fft
f = np.fft.fft(y)

print t.shape[-1]

#fftpack������ȿ��ӥ�κ���
freq = np.fft.fftfreq(t.shape[-1],1/sample_rate)


pl.plot(freq[:30],f.real[:30],"r")
pl.show()

pl.plot(freq[:30],f.imag[:30],"b")
pl.show()

pl.plot(freq[:30],np.abs(f[:30]))
pl.show()
