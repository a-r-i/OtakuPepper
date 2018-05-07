# -*- coding: utf-8 -*-
import time
import otaku

otaku = otaku.Otaku()

#0:00
#time.sleep(22)
#0:22
#for i in range(4):
#    otaku.speech("oi", 100)

#0:30 ここで曲認識すると仮定
otaku.speech("mix", 150)
time.sleep(59)
#1:43
for i in range(8):
    otaku.speech("oi", 100)
otaku.speech("mix_veryshort", 100)
time.sleep(16)
#2:12
otaku.speech("haisseno", 100)
time.sleep(92)
#3:48
for i in range(8):
    otaku.speech("oi", 250)
otaku.speech("mix_veryshort", 100)
time.sleep(18)
#4:17
otaku.speech("haisseno", 100)
time.sleep(22)
#4:42
otaku.speech("gachikoikojo", 100)
for i in range(4):
    otaku.speech("oi", 100)
otaku.speech("mix_short", 200)
otaku.speech("mix_japanese", 200)
otaku.speech("ainu", 100)