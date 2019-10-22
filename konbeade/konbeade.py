# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Fri May 19 10:47:18 2017

@author: _
"""

import cv
import cv2
import time
import numpy
import threading


DEVICE_ID = 0
SPEED = 1000
TIME_SPAN = 1
CASCADE = cv2.CascadeClassifier('cascade_hog.xml')
TIME = 0
S_KEY = 0
F_TXT = open('FB.txt','a')
B_TXT = open('Bin.txt','a')
CAP = cv2.VideoCapture(DEVICE_ID)
#xj = 0
KYORI = -295
GS = 0

def KEN(TIME,KYORI,FRAME,GS):
    FUSHI = CASCADE.detectMultiScale(FRAME, 1.1, 3)
    for (x, y, w, h) in FUSHI:     
        CENTER = (int(x+w/2), int(y+h/2))
        RADIUS = int(w/2+5)
        cv2.circle(FRAME, CENTER, RADIUS, cv.RGB(255,0,0), thickness = 3)
        xx = (x - 150) / 20.0
#        yy = y + 50 + (SPEED * TIME)
        yy = (y - 50 + KYORI) / 20.0 - 4 - GS
        w = w / 20.0
        h = h / 20.0
        xx = xx * 10
        yy = yy * 10
        w = w * 10
        h = h * 10
        print xx, yy, w, h
        F_TXT.write("%d,%d,%d,%d\n"%(xx, yy, w, h))
#	global xj
#	while xj < 110:
#		pixelValue = FRAME[315+xj,51]
#		pixelAverage = sum(pixelValue)/len(pixelValue)
#		print pixelAverage,
#		cv2.line(FRAME,(315+xj,51),(315+xj,55),(255,0,0),3)
#		if pixelAverage < 128:
#			B_TXT.write("0")
#			print "0"
#		else:
#			B_TXT.write("1")
#			print "1"
#		xj = xj + 11
#	xj = 0
    cv2.imwrite("%d.png"%TIME, FRAME)
    print "\n"
    F_TXT.write("\n")
    B_TXT.write("\n")
    

while True:
    ret,FRAME = CAP.read()
 #   while xj < 110:
#		cv2.line(FRAME,(310+xj,0),(310+xj,1000),(0,0,255),1)
	#	xj = xj + 11
    cv2.line(FRAME,(0,50),(1000,50),(0,0,255),1)
    cv2.line(FRAME,(150,0),(150,1000),(0,0,255),1)
 #   cv2.line(FRAME,(310,0),(310,1000),(0,0,255),1)
  #  cv2.line(FRAME,(321,0),(321,1000),(0,0,255),1)
   # cv2.line(FRAME,(332,0),(332,1000),(0,0,255),1)
    #cv2.line(FRAME,(343,0),(343,1000),(0,0,255),1)
#    cv2.line(FRAME,(354,0),(354,1000),(0,0,255),1)
#    cv2.line(FRAME,(365,0),(365,1000),(0,0,255),1)
#    cv2.line(FRAME,(376,0),(376,1000),(0,0,255),1)
#    cv2.line(FRAME,(387,0),(387,1000),(0,0,255),1)
#    cv2.line(FRAME,(398,0),(398,1000),(0,0,255),1)
#    cv2.line(FRAME,(409,0),(409,1000),(0,0,255),1)
#    cv2.line(FRAME,(420,0),(420,1000),(0,0,255),1)    
    KEY = cv2.waitKey(10)
    if KEY == ord('s'):
        S_KEY = 1
    if KEY == 27:
        F_TXT.close()
        break
    if S_KEY == 1:
#        THREAD = threading.Thread(target = KEN, args = (TIME,FRAME,))
        THREAD = threading.Thread(target = KEN, args = (TIME,KYORI,FRAME,GS,))
        THREAD.start()
        KYORI = KYORI + 295
        TIME += TIME_SPAN
        GS = GS + 0.5
#        KEN(TIME,FRAME)
        THREAD.join()
        time.sleep(TIME_SPAN)
    cv2.imshow('image',FRAME)
CAP.release()
cv2.destroyAllWindows()
