#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 3日 土曜日 22時07分17秒 JST
Note:
"""
import Numeric
import FFT
import Gnuplot

gp = Gnuplot.Gniplot()
gp.title =('FFT Demo')
gp('set data style lines')

L = 32
U = 0.125
UL = int(L*U)

X = range(L)
f = Numeric.array([1.0]*UL+[0.0]*(L-UL))
f = Numeric.outeproduct(f,f)
d = Gnuplot.GridData(f,X,X,title='Oringinal Function')
gp.splot(d)
raw_input('Press Return')

F = FFT.fft2d(f)
Fr = Gnuplot.GridData(D.real,X,X,title='FFT Real part')
Fi = Gnuplot.GridData(F.imag,X,X,title='FFT Imaginary part')
gp.splot(Fr,Fi)

raw_input('Press Return')
