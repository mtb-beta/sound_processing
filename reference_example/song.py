#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:kaiseki-web.lhd.nifs.ac.jp
Date:
2012ǯ 11�� 7�� ������ 17��21ʬ27�� JST
Note:this example code play song.wav
"""

import pyaudio
import wave

chunk=1024

filename = 'song.wav'
wf= wave.open(filename,'rb')
p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),channels =wf.getnchannels(),rate = wf.getframerate(),output =True)

remain = wf.getnframes()

while remain >0:
  s= min(chunk,remain)
  data = wf.readframes(s)
  stream.write(data)
  remain = remain -s
stream.close()
p.terminate()


