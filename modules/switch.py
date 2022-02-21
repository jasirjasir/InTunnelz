import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time


push_btn_last_state = True
        
def push_button_callback(channel):
    input_state = GPIO.input(26)
    global push_btn_last_state
    if input_state !=  push_btn_last_state :
        if input_state == False:
            print("Push button ON!")
        else:
            print("Push button OFF!")
    push_btn_last_state = input_state
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(26,GPIO.BOTH,callback=push_button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up


