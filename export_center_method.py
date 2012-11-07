#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012年 11月 7日 水曜日 11時36分02秒 JST
Note:センターをキャンセルした音源を原音を比較し、センターのみを抽出する。
"""


def export_center_file(filename,filename2):
  import wave
  import scipy as sci

  chunk =1024
  wf_in_default =wave.open(filename,'rb')
  wf_in_canseled_center= wave.open(filename2,'rb')
  output_file = 'center_'+filename
  wf_out =wave.open(output_file,'wb')
  wf_out.setnchannels(1)
  wf_out.setsampwidth(2)
  wf_out.setframerate(44100)
  remain = wf_in_default.getnframes()

  while remain >0:
    s = min(chunk,remain)
    data = wf_in_default.readframes(s)
    data2= wf_in_canseled_center.readframes(s)
    ary =sci.fromstring(data,sci.int16)
    ary2 =sci.fromstring(data2,sci.int16)
    #left =sci.int32(ary[::2])
    #right = sci.int32(ary[1::2])
    default_signal=sci.int32(ary[::])
    no_cr_signal=sci.int32(ary2[::])
    print len(default_signal)
    print len(no_cr_signal)
    new_ary=sci.int16(default_signal-no_cr_signal)
    new_data = new_ary.tostring()
    wf_out.writeframes(new_data)
    remain = remain-s
  wf_out.close()
  wf_in_default.close()
  wf_in_canseled_center.close()

if __name__ =="__main__":
  fname = "00.mix_NoEfect_SOZAI.wav"
  filename = "mono_"+fname
  filename2 = "CR_canselled_"+fname
  export_center_file(filename,filename2)
