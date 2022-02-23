import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time
import motor

skip_frame_count = 15
counter = 0

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    for obj in barcode:
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        if(barcodeData == "forward"):
            motor.motor1.rotate_forward()

def captureFrame():
    try:
        cap = cv2.VideoCapture(0)
        global counter
        while True:
            if counter == skip_frame_count: 
                ret, frame = cap.read()
                decoder(frame)
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                counter = 0
            else :
                ret = cap.grab() 
                counter += 1
    except cv2.error as e:
        print ("error while rading camera" , e)
            
