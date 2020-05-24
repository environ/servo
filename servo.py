# Raspberry Pi + MG90S Servo PWM Control Python Code
#
#
import RPi.GPIO as GPIO
import time

# setup the GPIO pin for the servo
servo_pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
def moveServo()

# setup PWM process
pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

#pwm.start(2.0) # start PWM by rotating to 90 degrees

start = 7.5 
end = 12.0
delta = 20.0

def moveServo():  #move from start to end, using delta number of seconds
     incMove=(end-start)/100.0
     incTime=delta/100.0
     for x in range(100):
          pi.set_servo_pulsewidth(4, int(start+x*incMove))
          time.sleep(incTime)

#pwm.ChangeDutyCycle(2.0) # rotate to 0 degrees
#time.sleep(2)
#pwm.ChangeDutyCycle(2.0) # rotate to 180 degrees
#time.sleep(2)
#pwm.ChangeDutyCycle(12.0) # rotate to 90 degrees
#time.sleep(2)

pwm.ChangeDutyCycle(0) # this prevents jitter
pwm.stop() # stops the pwm on 13
GPIO.cleanup() # good practice when finished using a pin
