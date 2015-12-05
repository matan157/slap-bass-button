""" 
    Matan Uchen
    Continuing with my RPi experiments...

    This program plays the Seinfeld Slap-Bass track on the press of
    a button. It will loop until released.

    It also lights an LED while the track is playing. Cause why not?
"""
from pygame import mixer
from gpiozero import Button, LED

def play():
    mixer.init()
    mixer.music.load('bass.mp3')
    mixer.music.play(-1)

def stop():
    mixer.music.stop()

""" These next two functions are there for the hell of it. """
def letThereBeLight():
    led.on()

def turnOffTheLight():
    led.off()

button = Button(2)
led = LED(17)


while True:
    button.wait_for_press()
    letThereBeLight()
    play()
    button.wait_for_release()
    turnOffTheLight()
    stop()
