#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 3日 土曜日 22時07分07秒 JST
Note:
"""
import Numeric
import FFT
import Gnuplot

gp = Gnuplot.Gnuplot()
gp.title = ('FFT Demo')
gp('set data style lines')

L = 128
U = 0.125
UL =int (L*U)

X =range(L)
f = Numeric.array([1.0]*UL+[0.0]*(L-UL))
d = Gnuplot.Data(X,f,title='Original Function')
gp.plot(d)

raw_input('Press Return')

F = FFt.ff(f)
Fr = Gnuplot.Data(X,F.real,title='FFT Real part')
Fi = Gnuplot.Data(X,F.imag,title='FFT Umaginary part')
gp.plot(Fr,Fi)

raw_input('Press Return')
