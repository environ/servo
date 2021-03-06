# Servo Control
import time
import wiringpi
 
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
 
# set #13 to be a PWM output
wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT)
 
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 0.01
 
#while True:
for pulse in range(55, 250, 1):
      wiringpi.pwmWrite(13, pulse)
      time.sleep(delay_period)
for pulse in range(250, 60, -1):
      wiringpi.pwmWrite(13, pulse)
      time.sleep(delay_period)
