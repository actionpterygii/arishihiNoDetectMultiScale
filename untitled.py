# -*- coding: utf-8 -*-
#!/usr/bin/env python

import cv
import cv2
import time
import numpy
import threading

DEVICE_ID = 0
TIME_SPAN = 0.5
TIME = 0
S_KEY = 0
GS = 233
F_TXT = open('FB.txt','w')
CAP = cv2.VideoCapture(DEVICE_ID)
CASCADE = cv2.CascadeClassifier('scascade.xml')

def KEN(TIME,FRAME,GS):
    FUSHI = CASCADE.detectMultiScale(FRAME, 1.1, 2)
    print TIME,"..."
    F_TXT.write("%s...\n"%TIME)
    n = 1
    for (x, y, w, h) in FUSHI:
        CENTER = (int(x+w/2), int(y+h/2))
        RADIUS = int(w/2+5)
        cv2.circle(FRAME, CENTER, RADIUS, cv.RGB(255,0,0), thickness = 3)
        xx = x / 20.0
        yy = y / 20.0
        w = w / 20.0
        h = h / 20.0
        xx = xx * 10
        yy = (yy * 10)+ (GS*(TIME*(TIME/(TIME+2))))
        w = w * 10
        h = h * 10
        print n,":" , xx,",", yy,",", w,",", h
        F_TXT.write("%d:%d,%d,%d,%d\n"%(n, xx, yy, w, h))
        n += 1
    cv2.imwrite("%s.png"%TIME, FRAME)
    print "\n"
    F_TXT.write("\n")

while True:
    ret,FRAME = CAP.read()

    height,width,chanels = FRAME.shape
    FRAME = FRAME[50:height-50,150:470]
   
    KEY = cv2.waitKey(10)
    if KEY == ord('s'):
        S_KEY = 1
    if KEY == 27:
        F_TXT.close()
        break
    if S_KEY == 1:
        THREAD = threading.Thread(target = KEN, args = (TIME,FRAME,GS,))
        time.sleep(TIME_SPAN)
        THREAD.start()
        TIME += TIME_SPAN
        THREAD.join()
    cv2.imshow('image',FRAME)
CAP.release()
cv2.destroyAllWindows()
