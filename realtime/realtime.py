# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 13:52:37 2016

@author: _
"""


import cv, cv2
# cv2.cv.CV_FOURCC
#def cv_fourcc(c1, c2, c3, c4):
#    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
#        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)


if __name__ == '__main__':
    
    ESC_KEY = 27     
    INTERVAL= 33     
    FRAME_RATE = 30  

   #ORG_WINDOW_NAME = "org"
    #FK_WINDOW_NAME = "fk"

    #GAUSSIAN_FILE_NAME = "gaussian.avi"

    DEVICE_ID = 0

    
    cap = cv2.VideoCapture(DEVICE_ID)

    
    end_flag, c_frame = cap.read()
    #height, width, channels = c_frame.shape
    #rec = cv2.VideoWriter(GAUSSIAN_FILE_NAME, \
                        #  cv_fourcc('X', 'V', 'I', 'D'), \
                        #  FRAME_RATE, \
                        #  (width, height), \
                        #  True)

    
   # cv2.namedWindow(ORG_WINDOW_NAME)
   # cv2.namedWindow(FK_WINDOW_NAME)
    
   # cascade = cv2.CascadeClassifier('cascade_lbp.xml')
  #  cascade = cv2.CascadeClassifier('cascade_haar.xml')
  #  cascade = cv2.CascadeClassifier('cascade_hog.xml')
   # cascade = cv2.CascadeClassifier('scascade_slbp.xml')
  #  cascade = cv2.CascadeClassifier('scascade_shaar.xml')
    cascade = cv2.CascadeClassifier('scascade_shog.xml')
   # scascade = cv2.CascadeClassifier('scascade_shaar.xml')
    
    #capture = cv.CaptureFromCAM(0)

    
    while end_flag == True:
        
       # g_frame = cv2.GaussianBlur(c_frame, (15, 15), 10)
        
        
        
        #img = cv.QueryFrame(capture)
    
        rt,im = cap.read()
        
        #g_frame = im
      #  sim = im
        
        #c_frame = cv2
        fushi = cascade.detectMultiScale(im, 1.1, 5) 
      #  sfushi = scascade.detectMultiScale(sim, 1.1, 3) 
        
       
        for (x, y, w, h) in fushi:
            print("%d%d%d%d" %(x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            c_frame = cv2.circle(im, center, radius, cv.RGB(255, 0, 0), thickness=3) 
            
    #    for (x, y, w, h) in sfushi:
     #       print("%d%d%d%d" %(x, y, w, h))
      #      scenter = (int(x+w/2), int(y+h/2))
       #     sradius = int(w/2+5)
        #    sc_frame = cv2.circle(sim, scenter, sradius, cv.RGB(255, 0, 0), thickness=3) 

        

        #while(cap.isOpened())
        #if g_frame == None:
         #   break
        
        cv2.imshow('ORG', im)
        
        #cv2.imshow('sORG', sim)
        
        #if g_frame is True:
           # cv2.imshow(FK_WINDOW_NAME, g_frame)


       # rec.write(g_frame)
        

        
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        
        c_frame = cap.read()
        
        
    cv2.destroyAllWindows()
    cap.release()
    #rec.release()
