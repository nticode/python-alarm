import _thread
import RPi.GPIO as GPIO
import time

from pygame import mixer
mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 26
GPIO_ECHO = 19


GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)
keepRunning = True
distance = 0

def measureDistance():
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = elapsed * 17150
    return distance

def playSound(threadName, delay):
    keepRunning
    distance
    while keepRunning:
        if distance <= 10:
            mixer.music.load("mixkit-facility-alarm-sound-999.wav")

            mixer.music.play(-1) # -1 to loop the sound
            time.sleep(10) #let it play for 10 seconds
            mixer.music.stop()
            time.sleep(0.01 * distance)               

try:
    distance = measureDistance()
    _thread.start_new_thread(playSound, ("mixkit-facility-alarm-sound-999.wav", 0.01))
    while True:
        print (distance)
        time.sleep(1)
        distance = measureDistance()
except:
    keepRunning = False
    time.sleep(1)
    GPIO.cleanup()
    

