#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def octave():
  BZ1 = 4    # BZ1 --> GPIO7(BCM:4,Physical:7)
  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # BZ1を出力に設定

  tonename = ['La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#']

  freq = 220.0    # 220Hz(低いラの音)
  buzzer = GPIO.PWM(BZ1, freq)
  buzzer.start(50)    # デューティ比 50 でPWM出力開始

  for i in range(0, 13):
    freq = 220.0 * (2 ** (i/12.0))
    print ('%3s : %.1f Hz' % (tonename[i%12], freq))
    buzzer.ChangeFrequency(freq)    # 周波数を変更
    time.sleep(0.2)

  buzzer.stop()
  GPIO.cleanup()

if __name__ == "__main__":
  octave()
