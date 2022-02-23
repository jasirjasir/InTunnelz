import RPi.GPIO as GPIO        
import time


class DCMotor:
    def __init__(self, in1=0, in2=0, en=0):
        self.in1 = in1
        self.in2 = in2
        self.en = en
        self.motor_status = "stop"
        self.setGPIO()
    
    def setGPIO(self) :
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.en,GPIO.OUT)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.pwm=GPIO.PWM(self.en,1000)
        self.pwm.start(80)


    def rotate_forward(self):
        print("Motor rotating forward")
        if(self.motor_status == "stop") : 
            GPIO.output(self.in1,GPIO.HIGH)
            GPIO.output(self.in2,GPIO.LOW)
            self.motor_status = "running"
            time.sleep(10)
            self.stop_motor()
        else :
            print("motor running status is  : " , self.motor_status)


    def rotate_backward(self):
        
        if(self.motor_status == "stop") : 
            print("Motor rotating backward")
            GPIO.output(self.in1,GPIO.LOW)
            GPIO.output(self.in2,GPIO.HIGH)
            time.sleep(10)
            self.motor_status = "running"
            self.stop_motor()
        else :
            print("motor running status is  : " , self.motor_status)

    def stop_motor(self):
        print("Motor stop")
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        self.motor_status = "stop"
    
    def speed_control(self, dutycycle):
        self.pwm.ChangeDutyCycle(dutycycle)

GPIO.setwarnings(False)
motor1 = DCMotor(23,24,25)
#motor1.rotate_forward()