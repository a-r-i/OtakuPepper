# encoding:UTF-8
import sys
import time
import commands
from datetime import datetime
import calendar

from naoqi import (ALProxy, ALBroker, ALModule)

PEPPER_IP = ""

PepperModule = None
memory = None

class PepperModuleClass(ALModule):
    def __init__(self, name):
        ALModule.__init__(self, name)
        #
        self.BIND_PYTHON( self.getName(),"callback" )
        self.tts = ALProxy("ALTextToSpeech", PEPPER_IP, 9559)
        #
        print("PepperModule Initialyze")

    def startRecord(self):
        # self.tts.say("録音を開始します")
        #
        # ファイルの保存先設定
        self.saveFile = open("./sounds/pepper_record.raw","wb")
        self.pepperMicrophone = ALProxy("ALAudioDevice", PEPPER_IP, 9559)
        #
        # 16KHzのモノラル音声でFront(3)マイク１つのみを指定
        self.pepperMicrophone.setClientPreferences(self.getName(), 16000, 3, 0)
        #
        # 録音開始
        self.pepperMicrophone.subscribe(self.getName())

    def processRemote(self, inputChannels, inputSamples, i, inputBuff):
        # 録音バッファを保存
        self.saveFile.write(inputBuff)

    def stopRecord(self):
        # 録音終了
        self.pepperMicrophone.unsubscribe(self.getName())
        self.saveFile.close()
        commands.getoutput("sox -r 16000 -b 16 -e signed-integer ./sounds/pepper_record.raw ./sounds/pepper_record.wav") #raw→wav変換
        check = commands.getoutput("python audfprint.py match --dbase fpdbase.pklz ./sounds/pepper_record.wav") #録音データをデータベースに照合。実行結果を変数に格納する。
        return check

def main():

    myBroker = ALBroker("myBroker","0.0.0.0",0,PEPPER_IP,9559)

    global PepperModule
    PepperModule = PepperModuleClass("PepperModule")

    while True:
        #録音開始
        PepperModule.startRecord()

        # 30秒録音
        time.sleep(30)

        #録音終了
        check = PepperModule.stopRecord()

        index = check.find("satellite") #実行結果にファイル名が含まれているか検索
        if index != -1: #ファイル名が含まれている = 曲が見つかったら
            commands.getoutput("/usr/bin/python satellite.py") #アイドルオタク化プログラムを実行
            myBroker.shutdown()
            sys.exit(0)
        else:
            print "not found"

if __name__ == "__main__":
    main()