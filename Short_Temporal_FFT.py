#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 3日 土曜日 22時08分27秒 JST
Note:
"""
import wave
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt
import math
from pylab import*
from numpy import*
import pyaudio
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pylab

sampling = 44100.0
set_chunk= 1024

def read_wave_sample(filename):

  import transport_mono_method as tm

  tmp = wave.open(filename,'rb')

  if tmp.getnchannels()!=1:
    tm.transport_mono_file(filename)
    fname = "mono_"+filename
  else:
    fname =filename


  #open object wav file
  wf = wave.open(fname,'rb')

  #all data read frame.getnframes() return all frame number in wf object.
  data= wf.readframes(wf.getnframes())

  #fromstring() is data which is text or binary transport format int16.
  ary=sp.fromstring(data,sp.int16)

  #return the list which is 2^16
  return ary


"""
argment,object wave(filename)
stft(short time flouir transport )method by haming window.
window size given chunk.
return freq power by dB(numpy.array)
"""
def self_stft(filename,chunk):
  #read .wav file's  all frames.
  read_ary = read_wave_sample(filename)

  #chunk,sampled sumed.
  n = chunk

  #over rap rate
  num = 4

  frame_size = chunk/num
  T = int(len(read_ary)/frame_size)#フレームの総数
  window = sp.signal.get_window('hamming',chunk)#窓の定義

  m = chunk/2
  p =array([ones(m)])


  #全てのフレームについてSTFT
  for i in range(T-num+1):

    #FFTを行うサンプル群を抜き出し窓関数を書ける。
    fft_sample = read_ary[frame_size*i:frame_size*i+chunk]*window

    #FFTを行う
    tmp= fft.fft(fft_sample)

    #実数部の半分を取り出す。
    tmp=tmp[0:m]

    #スペルトルをパワーに変換
    tmp=abs(tmp)

    #オーバーラップした部分の平均を取る計算。本当はこんな漢字でif文で書くのではなく、
    #キューを用いて汎用性のあるプログラムにする方が望ましいが、
    #その実装は現段階では言及せずに、実験段階で実装する予定とする。
    if i==0 or i==(T-num):
      stored_fft = tmp
      over_tmp1 = tmp
    elif i==1:
      over_tmp2 = tmp
      stored_fft = (over_tmp1+over_tmp2)/2
    elif i==2:
      over_tmp3 = tmp
      stored_fft = (over_tmp1+over_tmp2+over_tmp3)/3
    elif i==3:
      over_tmp4 = tmp
      stored_fft = (over_tmp1+over_tmp2+over_tmp3+over_tmp4)/4
    elif i== (T-num-2):
      over_tmp2 = over_tmp3
      over_tmp3 = over_tmp4
      over_tmp4 = tmp
      stored_fft = (over_tmp1+over_tmp2+over_tmp3+over_tmp4)/3
    elif i==(T-num-1):
      over_tmp3 = over_tmp4
      over_tmp4 = tmp
      stored_fft = (over_tmp1+over_tmp2+over_tmp3+over_tmp4)/2
    else:
      over_tmp1 = over_tmp2
      over_tmp2 = over_tmp3
      over_tmp3 = over_tmp4
      over_tmp4 = tmp
      stored_fft = (over_tmp1+over_tmp2+over_tmp3+over_tmp4)/4


    #今回の結果をpに追加
    p = vstack((p,stored_fft))

  #スペクトログラムを返す
  return log2(p)


"""
2次元濃淡グラフの生成
第１引数がx軸、第２引数がy軸、第3引数が濃淡
"""
def fig_make(chunk,p):
  
  T=len(p)
  freq = fft.fftfreq(chunk,1/sampling)
  t=arange(0,T,1)
  t = 1000/(sampling/(chunk/4))*t#軸をmsに変更
  
  X,Y = meshgrid(t,f)#numpy
  Z=p.T
  
  print X.ndim
  print Y.ndim
  print Z.ndim
  print len(X)
  print len(Y)
  print len(Z)
  
  fig = plt.figure()
  
  ax = fig.add_subplot(111)#colorグラフ用概形
  cax = ax.imshow(Z, interpolation='nearest')
  ax.set_title('spectrogram with vertical colorbar')#title
  
  cbar.ax.set_yticklabels(['< -1', '0', '> 1'])# vertically oriented colorbar
  
  plt.show()
  
"""
周波数スペクトルの書き出し
"""
def out_freq(chunk,p,filename):
  filename2 = (str)(filename)+"_FFT.txt"
  f =open(filename2,'w')
  print "start print out spectrogram."


  fft.fftfreq(chunk,1.0/sampling)
  counter = 0
  lenp = len(p)
  for i in range(lenp):
    if(i > lenp/100*counter):
      print "processing "+(str)(counter)+"%."
      counter= counter +1
    for j in range(len(p[i])-1):
      f.write(str(p[i][j])+',')
    f.write(str(p[i][len(p[i])-1])+'\n')
  f.close()
  
  #import os
  #os.system("mv "+filename2+" ./data")

def stft(filename,chunk):
  return self_stft(filename,chunk)


def print_syntax_IOE():
    print "SyntaxError:invalid syntax."
    print "Please type object .wav file."
    print "We hope you type this program with .wav file."
    print "Command format is \n python [this file] [object .wav file]."
    exit()

if __name__=='__main__':
  from sys import argv #get argv module
  from os.path import splitext #to get file format module

  Command = argv #comand line argment list
  chunk=set_chunk

  print "This STFT program adopted window size "+str(chunk)+"."

  if(len(Command) != 2):
    print_syntax_IOE()
  else:
    filename,format =splitext(Command[1])
    if (format != '.wav'):
      print_syntax_IOE()

  p=self_stft(filename+".wav",chunk)	
  out_freq(chunk,p,filename)
  #fig_make(chunk,p)
