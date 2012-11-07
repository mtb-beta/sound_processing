#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012ǯ 11�� 3�� ������ 22��06ʬ52�� JST
Note:
"""

import scipy as sp
import pylab as pl

#����ץ�졼�Ȥ�1000�Ȥ��롣
sample_rate=1000.00

#�����飰�����δ֤�0.001�ֳ֤��ͤ�����롣
t=sp.r_[0:0.6:1/sample_rate]

#����ץ�ο����ǧ
N=len(t)

#����ץ�Ȥʤ��Ȥ����
s=sp.sin(2*sp.pi*50*t) + sp.sin(2*sp.pi*70*t+sp.pi/4)

#����ץ��Ȥ��ǧ
pl.plot(t,s)
pl.show()


#����ץ��Ȥ�FFT
S=sp.fft(s)

#���ȿ��ӥ�����
f=sample_rate*sp.r_[0:(N/2)]/N

#���ȿ��ӥ�ο����ǧ
n=len(f)

#FFT�η�̤�Ļ벽
pl.plot(f,abs(S[0:n])/N)
pl.show()
