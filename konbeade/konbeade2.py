# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:47:18 2017

@author: _
"""

import cv, cv2, time, threading

DEVICE_ID = 1
SPEED =1000
TIME_SPAN = 1
CASCADE = cv2.CascadeClassifier('cascade_hog.xml')
TIME = 0
S_KEY = 0
F_TXT = open('FB.txt','a')
CAP = cv2.VideoCapture(DEVICE_ID)
FPS = CAP.get(cv2.cv.CV_CAP_PROP_FPS)
FRAME_SPAN = TIME_SPAN * 30
COUNT = 0

def KEN(TIME,FRAME):
#    FUSHI = CASCADE.detectMultiScale(FRAME, 1.1, 3)
 #   for (x, y, w, h) in FUSHI:
  #      print x, y, w, h
   #     CENTER = (int(x+w/2), int(y+h/2))
    #    RADIUS = int(w/2+5)
     #   cv2.circle(FRAME, CENTER, RADIUS, cv.RGB(255,0,0), thickness = 3)
      #  xx = x + 50 + (SPEED * TIME)
       # yy = y + 50
        #F_TXT.write("%d,%d,%d,%d\n"%(xx, yy, w, h))
    cv2.imwrite("%d.png"%TIME, FRAME)
    F_TXT.write("\n")

while True:
    ret,FRAME = CAP.read()
    cv2.line(FRAME,(0,50),(1000,50),(0,0,255),1)
    cv2.line(FRAME,(400,0),(400,1000),(0,0,255),1)
    cv2.imshow('image',FRAME)
    KEY = cv2.waitKey(10)
    if KEY == ord('s'):
        S_KEY = 1
    if KEY == 27:
        F_TXT.close()
        break
    if S_KEY == 1:
		COUNT += 1
		if COUNT > FRAME_SPAN -1:
			if TIME != 0:
				THREAD.join() 
			THREAD = threading.Thread(target = KEN, args = (TIME,FRAME,))
#			KEN(TIME,FRAME)
			THREAD.start()
			TIME += TIME_SPAN
			COUNT = 0
			    
CAP.release()
cv2.destroyAllWindows()
