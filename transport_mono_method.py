#!/usr/bin/env python
#-*-coding:utf-8-*-
"""
Author:mtb_beta
Date:
2012ǯ 11�� 3�� ������ 22��06ʬ20�� JST
Note:This method is that stereo wave file transport mono wave file
"""

#main method
def transport_mono_file(filename):
  import wave
  import scipy as sci

  # chunk is number processing at a time
  chunk =1024

  # wf_in is input stereo wave file
  wf_in =wave.open(filename,'rb')

  # output file name
  output_file = 'mono_'+filename

  # preparation output wave file
  wf_out =wave.open(output_file,'wb')

  # output file is mono
  wf_out.setnchannels(1)

  # output file is 16bit samples
  wf_out.setsampwidth(2)

  # output file's sample rate is 441000.
  wf_out.setframerate(44100)

  # remain is input file's frame sum.
  remain = wf_in.getnframes()

  #repeat input file frame end
  while remain >0:
    # check object frame remain chunk
    s = min(chunk,remain)

    # data is read frame
    data = wf_in.readframes(s)

    # data transport numpy.int16 because data is string.
    ary =sci.fromstring(data,sci.int16)

    # L and R pull each signal
    left =sci.int32(ary[::2])
    right = sci.int32(ary[1::2])

    # ary2 is mean L and R signal power.
    ary2=sci.int16((left+right)/2)

    # Because ary2 is int16,it transport string and substitute data2.
    data2 = ary2.tostring()

    # output file add a postscript which data2
    wf_out.writeframes(data2)

    # remain substract already process data.
    remain = remain-s
  wf_out.close()
  wf_in.close()

if __name__=="__main__":
  filename = "mix_sample.wav"
  transport_mono_file(filename)
