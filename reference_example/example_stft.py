#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:kaiseki-web.lhd.nifs.ac.jp
Date:2012年 11月 7日 水曜日 18時19分55秒 JST
Note:example stft and ifft
"""

import wave
import scipy as sp

WINSIZE = 256
infile='song.wav'
outfile='out.wav'

def read_signal(filename,winsize):
  wf = wave.open(filename,'r')
  n = wf.getnframes()
  str = wf.readframes(n)
  params = ((wf.getnchannels(),wf.getsampwidth(),wf.getframerate(),wf.getnframes(),wf.getcomptype(),wf.getcompname()))
  siglen = ((int )(len(str)/2/winsize) + 1)*winsize
  signal = sp.zeros(siglen,sp.int16)
  signal[0:len(str)/2] = sp.fromstring(str,sp.int16)
  return [signal,params]

def get_frame(signal,winsize,no):
  shift = WINSIZE/2
  start = no*shift
  end =start +WINSIZE
  return signal[start:end]

def add_signal(signal,frame ,winsize,no):
  shift=winsize/2
  start = no*shift
  end =start+winsize
  signal[start:end] = signal[start:end] +frame
def write_signal(filename,params,signal):
  wf =wave.open(filename,'w')
  wf.setparams(params)
  s = sp.int16(signal).tostring()
  wf.writeframes(s)

signal,params =read_signal(infile,WINSIZE)
nf = len(signal)/(WINSIZE/2)-1
sig_out =sp.zeros(len(signal),sp.float32)
window = sp.hanning(WINSIZE)

for no in xrange(nf):
  y = get_frame(signal,WINSIZE,no)
  Y = sp.fft(y*window)

  y_o =sp.real(sp.ifft(Y))
  add_signal(sig_out,y_o,WINSIZE,no)

write_signal(outfile,params,sig_out)
