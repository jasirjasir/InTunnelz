import RPi.GPIO as GPIO
import time
import motor
import multiprocessing


push_btn_last_state = True
button_pin = 26
 
def pushButton_callback(channel):
    input_state = GPIO.input(26)
    global push_btn_last_state
    if input_state !=  push_btn_last_state :
        if input_state == False:
            print("Push button ON!")
            motor.motor1.rotate_forward()
            #process = multiprocessing.Process(target=motor.motor1.rotate_forward())
            #proces.start()
            #print("Executing after multiProcess!")
        else:
            print("Push button OFF!")
    push_btn_last_state = input_state

def setupButton():  
     
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
    GPIO.add_event_detect(button_pin,GPIO.BOTH,callback=pushButton_callback) 


