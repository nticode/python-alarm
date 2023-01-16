import RPi.GPIO as GPIO
import time

import datetime

import requests
url = "http://ip:5000/api/create"

from pygame import mixer
mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 26
GPIO_ECHO = 19


GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)
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
            
while True:
    time.sleep(1)
    distance = measureDistance()
    if distance <= 10:
        mixer.music.load("mixkit-facility-alarm-sound-999.wav")
        
        now = datetime.datetime.now()
        requests.post(url, params = {
            "time": now.strftime("%Y-%m-%d"),
            "timestamp": now.strftime("%Y-%m-%d %H-%M %S"),
            "distance": distance
        })

        #mixer.music.play(-1) # -1 to loop the sound
        #time.sleep(10) #let it play for 10 seconds
        #mixer.music.stop()
        time.sleep(0.01 * distance)
        
    print(distance)
