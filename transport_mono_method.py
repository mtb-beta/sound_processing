#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 3日 土曜日 22時06分20秒 JST
Note:ステレオで入力されたwavファイルをモノラルに変換するメソッド
"""

def transport_mono_file(filename):
  import wave
  import scipy as sci

  chunk =1024
  wf_in =wave.open(filename,'rb')

  output_file = 'mono_'+filename
  wf_out =wave.open(output_file,'wb')
  wf_out.setnchannels(1)
  wf_out.setsampwidth(2)
  wf_out.setframerate(44100)
  remain = wf_in.getnframes()

  while remain >0:
    s = min(chunk,remain)
    data = wf_in.readframes(s)
    ary =sci.fromstring(data,sci.int16)
    left =sci.int32(ary[::2])
    right = sci.int32(ary[1::2])
    ary2=sci.int16((left+right)/2)
    data2 = ary2.tostring()
    wf_out.writeframes(data2)
    remain = remain-s
  wf_out.close()
  wf_in.close()

if __name__=="__main__":
  filename = "mix_sample.wav"
  transport_mono_file(filename)
