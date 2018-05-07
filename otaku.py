# -*- coding: utf-8 -*-
from naoqi import (ALProxy, ALBroker, ALModule)
import time

PEPPER_IP = ""
PORT = 9559

phrases = {"call": "おーれーのーーー点ちゃーーーん！",
         "oi": "おい！",
         "syaaikuzo": "しゃーーーーー！いくぞー！",
         "ikkuzo": "いっくっぞーーーーー！",
         "mix": "タイガ！ファイヤ！サイバ！ファイバ！ダイバー！バイバー！ジャーーージャーーー！"
                "ファイボ！ワイパ！ファーマ！ジャスパ！ホワイパー！クーパー！イエスクレイパーーー！",
        "mix_short": "タイガ！ファイヤ！サイバ！ファイバ！ダイバー！バイバー！ジャーーージャーーー！",
        "mix_veryshort": "イエッタイガファイボワイパア！",
        "mix_last": "タイガファイヤサイバファイバダイババイバージャーーージャーーーーーーーーーーーーーーーーーーーーーーー！！！！！",
         "mix_japanese": "虎！火！人造！繊維！海女！振動！化繊！",
        "ainu": "チャペ！アペ！カラ！キナ！ララ！トゥスケ！ウィスパー！ケスィ！スィスパーーーー！",
        "madaikanai": "まだ行かない！",
         "imadesyo": "いつ行くのー？いまでしょー",
         "haisseno": "はいっせーの！はーいはい！はいはいはいはい！",
        "haihai": "はーいはい！はいはいはいはい！",
         "gachikoikojo": "言いたいことがああるんだよお！　やっぱり点ちゃんかわいいよお！　すきすき大好きやっぱ好きい！　やっとぉ見つけたお姫様あ！"
                         "俺がぁ生まれてきた理由！　それはあ点ちゃんに出会うため！　俺とお一緒に人生歩もう、世界で一番愛してる！　あいしてるーーーーー！！！",
         "oing": "オーイングッ！",
         "o": "オーーーーーーー！",
         "formation": "このフォーメーションは！！！！！！！！！",
         "request_lift": "あげろあげろーーーーーーーーーーー！！！！！！！！！！"
         }

try:
    tts = ALProxy("ALTextToSpeech", PEPPER_IP, PORT)
except Exception,e:
    print(e)

try:
    motion = ALProxy("ALMotion", PEPPER_IP, PORT)
except Exception,e:
    print(e)

try:
    animation_player = ALProxy("ALAnimationPlayer", PEPPER_IP, PORT)
except Exception,e:
    print(e)

try:
    bAwareness = ALProxy("ALBasicAwareness", PEPPER_IP, PORT)
except Exception,e:
    print(e)

try:
    alifeMove = ALProxy("ALAutonomousMoves", PEPPER_IP, PORT)
except Exception,e:
    print(e)

class Otaku():

    def __init__(self):
        print("")

    def wake_up(self):
        motion.wakeUp()

    def autonomouslife_off(self):
        bAwareness.stopAwareness()
        alifeMove.setBackgroundStrategy("none")
        alifeMove.setExpressiveListeningEnabled(False)

    def autonomouslife_on(self):
        bAwareness.startAwareness()
        alifeMove.setBackgroundStrategy("backToNeutral")
        alifeMove.setExpressiveListeningEnabled(True)

    def setting(self):
        motion.setOrthogonalSecurityDistance(0.0)
        motion.setTangentialSecurityDistance(0.0)
        motion.setExternalCollisionProtectionEnabled("RArm", False)
        motion.setExternalCollisionProtectionEnabled("LArm", False)
        motion.setAngles(["RShoulderPitch"], [1.5], 0.1)
        time.sleep(1)
        motion.setAngles(["LShoulderPitch"], [1.5], 0.1)

    def speech(self, title, speed_value):
        tts.say("\\rspd=%s\\%s" % (speed_value,phrases[title]))

    def kecak(self):
        for i in range(8):
            motion.setAngles(["RShoulderPitch"], [-0.5], 0.1)
            time.sleep(1)
            motion.setAngles(["LShoulderPitch"], [-0.5], 0.1)
            time.sleep(3)
            # motion.wakeUp()
            motion.setAngles(["RShoulderPitch"], [0.3], 0.1)
            time.sleep(1)
            motion.setAngles(["LShoulderPitch"], [0.3], 0.1)

        motion.setAngles(["RShoulderPitch"], [1.5], 0.1)
        time.sleep(1)
        motion.setAngles(["LShoulderPitch"], [1.5], 0.1)

    def point_a_finger(self):
        animation_player.run("animations/Stand/Gestures/Far_3")
        time.sleep(50)
        motion.setAngles(["RShoulderPitch"], [1.5], 0.1)
        time.sleep(1)
        motion.setAngles(["RShoulderPitch"], [1.5], 0.1)