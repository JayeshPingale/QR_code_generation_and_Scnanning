import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img=cv2.imread("2.png")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

with open('myDatafile.txt') as f:
    myDatalist = f.read().splitlines()

camera= True
while camera==True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDatalist:
            myOutput='authorized'
            myColor=(0,255,0)
            print(myOutput)
        else:
             myOutput='un-authorized'
             myColor=(0,0,255)
             print(myOutput)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        thickness = 2
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), font, fontScale, myColor, thickness)
    cv2.imshow('output', img)
    cv2.waitKey(1)
