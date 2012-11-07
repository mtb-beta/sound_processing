#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 7日 水曜日 11時22分09秒 JST
Note:ステレオwavファイルの左右の音の差をとる事でセンターの音を抽出する。
"""
def canselled_center_method(filename):
  import wave
  import scipy as sci

  chunk =1024
  wf_in =wave.open(filename,'rb')

  output_file = 'CR_canselled_'+filename
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
    #ary2_left = sci.int32(left-right)
    #ary2_right= sci.int32(right-left)
    ary2_left = sci.int16(left-right)
    ary2_right= sci.int16(right-left)
    ary3 = sci.empty(len(ary2_left)+len(ary2_right))
    for i in range(len(ary2_left)):
      ary3[i]=ary2_left[i]
      ary3[i+1]=ary2_right[i]
    ary3 = sci.int16(ary3)
    #ary3 =sci.int16(ary2)#確認
    data2 = ary3.tostring()
    wf_out.writeframes(data2)
    remain = remain-s
  wf_out.close()
  wf_in.close()

if __name__ =="__main__":
  filename = "00.mix_NoEfect_SOZAI.wav"
  canselled_center_method(filename)
