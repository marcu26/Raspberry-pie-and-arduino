#! /usr/bin/python
from numpy import angle
from guizero import App, PushButton, Text, TextBox
import serial
import time
import sys

angle="90"

def exitApp():
    ser.write(b"exit\n")
    sys.exit()


ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
ser.reset_input_buffer()


def showAll():
    exitButton.show()
    moveServoButton.show()
    pastrezaDistantaButton.show()
    jocReflexButton.show()
    _6din49Button.show()
    rollDiceButton.show()
    silenceButton.show()




def exitFromModule():
    ser.write(b"exit\n")
    text.hide()
    exitFuncButton.hide()
    moveServoButton.hide()
    sendButton.hide()
    input_box.hide()
    showAll()



def hideAll():
    _6din49Button.hide()
    jocReflexButton.hide()
    exitButton.hide()
    pastrezaDistantaButton.hide()
    text.hide()
    moveServoButton.hide()
    rollDiceButton.hide()
    silenceButton.hide()

def option_6din49():
    ser.write(b"5\n")

def option_jocReflex():
    ser.write(b"3\n")
   # while ser.in_waiting < 0:
   #     print("ok")
   # line = ser.readline().decode('utf-8').rstrip()
   # hideAll()
   # text.clear()
   # text.append("scor:"+line)
   # text.show()
    

def option_moveServo():
    ser.write(b"6\n")
    setDistanceText()
    hideAll()
    text.show()
    input_box.show()
    exitFuncButton.show()
    sendButton.show()

def sendZaruri():
    toSend=input_box.value+"\n"
    ser.write(toSend.encode('utf-8'))
    sendButton2.hide()
    input_box.hide()
    showAll()

def option_rollDice():
     ser.write(b"4\n")
     hideAll()
     input_box.show()
     sendButton2.show()

def option_Silence():
    hideAll()
    ser.write(b"2\n")
    text.clear()
    text.append("Senzor audio activat")
    text.show()
    exitFuncButton.show()


def getInputForMotor():
    global angle
    angle=input_box.value
    angle=angle+"\n"
    ser.write(angle.encode('utf-8'))
    setDistanceText()

def setDistanceText():
    line = ser.readline().decode('utf-8').rstrip()
    text.clear()
    text.append("Distanta pana la senzor:" + line)




def option_pastreazaDistanta():
    hideAll()
    ser.write(b"1\n")
    text.clear()
    text.append("Senzor distanta activat")
    text.show()
    exitFuncButton.show()
   # ser.write(b"giveMe\n")
   # line = ser.readline().decode('utf-8').rstrip()
   # text1.clear()
   #  text1.append(line)



app=App('ControlerGUI', height = 600, width = 800)

text=Text(app,text="ceva")
text.hide()
text.text_size=30



moveServoButton = PushButton(app, option_moveServo,text="Move Servo", align="top", width=10, height=1)
moveServoButton.text_size=15


pastrezaDistantaButton = PushButton(app, option_pastreazaDistanta,text="Pastreaza dist", align="top", width=10, height=1)
pastrezaDistantaButton.text_size=15


jocReflexButton = PushButton(app, option_jocReflex,text="Joc reflex", align="top", width=10, height=1)
jocReflexButton.text_size=15

_6din49Button = PushButton(app, option_6din49,text="6 din 49", align="top", width=10, height=1)
_6din49Button.text_size=15

rollDiceButton = PushButton(app, option_rollDice,text="Roll dice", align="top", width=10, height=1)
rollDiceButton.text_size=15

silenceButton = PushButton(app, option_Silence,text="Fa liniste", align="top", width=10, height=1)
silenceButton.text_size=15



exitButton= PushButton(app,exitApp,text="Exit", align="bottom", width=10, height=1)
exitButton.text_size=15

exitFuncButton= PushButton(app,exitFromModule,text="Exit", align="bottom", width=10, height=1)
exitFuncButton.text_size=15
exitFuncButton.hide()

sendButton=PushButton(app,getInputForMotor,text="Send", align="bottom", width=10, height=1)
sendButton.text_size=15
sendButton.hide()

sendButton2=PushButton(app,sendZaruri,text="Send", align="bottom", width=10, height=1)
sendButton2.text_size=15
sendButton2.hide()




input_box = TextBox(app, text="", multiline=False)
input_box.hide()

app.display()
