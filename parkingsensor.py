
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
TRIG = 4
ECHO = 18
GREEN = 17
YELLOW = 27
RED = 22
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)
def green_light():
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(RED, GPIO.LOW)
def yellow_light():
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.HIGH)
        GPIO.output(RED, GPIO.LOW)
def red_light():
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.LOW)
        GPIO.output(RED, GPIO.HIGH)
def get_distance():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO) == False: start = time.time()
	while GPIO.input(ECHO) == True: end = time.time()
	signal_time = end-start
	distance = signal_time / 0.000058
	return distance
while True:
        distance = get_distance()
        time.sleep(0.05)
        
        if distance >= 25:
                green_light()
                print ("keep going")
        elif distance < 25 and distance > 10:
                yellow_light()
                print("A little Farther")
        elif distance <= 9:
                red_light()
                print("Stop")
