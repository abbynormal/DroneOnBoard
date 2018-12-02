import pigpio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(3,GPIO.OUT)

pi = pigpio.pi()

def pwm_init() :
        pi.set_servo_pulsewidth(17, 2000)
        time.sleep(2)
        pi.set_servo_pulsewidth(17, 1000)
        time.sleep(2)

	pi.set_servo_pulsewidth(27, 2000)
        time.sleep(2)
        pi.set_servo_pulsewidth(27, 1000)
        time.sleep(2)

def pwm_cleanup() :
        pi.set_servo_pulsewidth(27,0)
        pi.set_servo_pulsewidth(17,0)
        pi.stop()
        GPIO.cleanup()

pwm_init()


for i in range(1000, 1700, 100):
	print i
	pi.set_servo_pulsewidth(17, i)
        pi.set_servo_pulsewidth(27,i)
	time.sleep(2)

pwm_cleanup()
