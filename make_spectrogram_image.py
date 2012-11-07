#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 3日 土曜日 22時36分05秒 JST
Note:
"""
import Image as im
import numpy as np

wigth_size = 1
hight_size = 1
sample_rate = 44100.0
"""
Note:
"""
def read_spectrogram_csv(filename):
  f = open(filename)
  data= np.loadtxt(filename,delimiter=',')
  return data

def make_new_image(data,chunk):
  width = len(data)*wigth_size

  _freq=np.fft.fftfreq(t)
  height = len(data[0])*hight_size

  #print width
  #print height
  img = im.new('RGB',(width,height),(0,0,0))

  return img

def draw_spectrogram_image(data,img):
  max_data = np.max(data)
  for t in range(len(data)):
    print "t"+str(t)
    for f in range(len(data[t])):
      color = data[t,f]/max_data*256
      Colors = (color,color,0)
      img.putpixel((t,f),Colors)

      """
      if(data[t,f]/max_data>0.9):
        Colors = (200,20,20)
      elif(data[t,f]/max_data>0.8):
        r,g,b=HSV2RGB(data[t,f]/max_data*360,100,150)
        #print data[t,f]/max_data*360
        #print "R,G,B:"+str(r)+','+str(g)+','+str(b)
        Colors=(r,g,b)
      else:
        Colors=(0,0,0)
      for p in range(wigth_size):
        for y in range(hight_size):
          img.putpixel((t*wigth_size+p,f*hight_size+y),Colors)
      """
  return img

def make_fig_plt(data,chunk):
  import matplotlib.pyplot as plt

  t = np.arange(0,len(data),1)*(1/sample_rate)*(chunk/4)
  freq = np.arange(0,chunk/2,1)*(sample_rate/chunk)*100

  X,Y= np.meshgrid(t,freq)
  print len(freq)
  print len(data)

  Z=data.T

  fig = plt.figure()
  ax = fig.add_subplot(111)
  cax = ax.imshow(Z,interpolation ='nearest')
  ax.set_title('spectrogram with vertical calorbar')
  cbar = fig.colorbar(cax,ticks=[-1,0,1])
  cbar.ax.set_yticklabels(['< -1','0','> 1'])
  #plt.plot(freq,10*np.log10(data))
  plt.show()
  exit()

def make_spectrogram_image(filename,chunk):
  data = read_spectrogram_csv(filename)

  """
  Note:テスト的にとりあえず外部関数を利用して描画してみる。
  """
  make_fig_plt(data,chunk)

  img = make_new_image(data,chunk)
  img = draw_spectrogram_image(data,img)

  img.show()
  image_name=filename+".jpg"
  img.save(image_name,"JPEG")

def HSV2RGB(h,s,v):
  r=0
  g=0
  b=0
  if(s==0):
    r=v
    g=v
    b=v
  else:
    hi = int(h/60)
    f  = h/60.0-hi
    p  = v *(1-s)
    q = v * ( 1 - f * s )
    t = v * ( 1 - ( 1 - f ) * s )
    #print "hi,f,p,q,t:"+str(hi)+','+str(f)+'.'+str(p)+','+str(q)+','+str(t)
    if hi == 0:
      r = int(round( v ))
      g = int(round( t ))
      b = int(round( p ))
    elif hi == 1:
      r = int(round( q ))
      g = int(round( v ))
      b = int(round( p ))
    elif hi == 2:
      r = int(round( p ))
      g = int(round( v ))
      b = int(round( t ))
    elif hi == 3:
      r = int(round( p ))
      g = int(round( q ))
      b = int(round( v ))
    elif hi == 4:
      r = int(round( t ))
      g = int(round( p ))
      b = int(round( v ))
    elif hi == 5:
      r = int(round( v ))
      g = int(round( p ))
      b = int(round( q ))
    #print 'r,g,b:'+str(r)+','+str(g)+','+str(b)
  return r, g, b



if __name__=='__main__':
  from sys import argv
  from os.path import splitext
  Command = argv

  if(len(argv) !=3):
    filename = "00.mix_NoEfect_SOZAI_FFT.txt"
    chunk =1024
    #filename = "mix_sound_FFT.txt"
  else:
    chunk = argv[2]
    filename = argv[1]
  make_spectrogram_image(filename,chunk)

  

