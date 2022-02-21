import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import time
import matplotlib.pyplot as plt

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)

cap = cv2.VideoCapture(0)
target = 15
counter = 0
showframe = True
plt.show()
while True:
    if counter == target: 
        ret, frame = cap.read()
        decoder(frame)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show(block=False)
        counter = 0
    else :
        ret = cap.grab() 
        counter += 1 
        