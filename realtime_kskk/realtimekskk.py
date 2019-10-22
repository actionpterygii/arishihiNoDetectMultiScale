# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 13:52:37 2016

@author: _
"""


import cv, cv2, numpy as np
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
    
    cascade = cv2.CascadeClassifier('cascade_hog.xml')
    
    #capture = cv.CaptureFromCAM(0)
    
    rt,org_im = cap.read()
    
    """
    if len(org_img.shape) == 3:
		height, width, channels = org_img.shape[:3]
	else:
		height, width = org_img.shape[:2]
		channels = 1
	zeros = np.zeros((height, width), org_img.dtype)
	"""
    
    while end_flag == True:
        
       # g_frame = cv2.GaussianBlur(c_frame, (15, 15), 10)
        
        
        
        #img = cv.QueryFrame(capture)
    
        rt,org_im = cap.read()
        
        #g_frame = im
        
        #c_frame = cv2
        
        ##
        gry_im = cv2.cvtColor(org_im, cv2.COLOR_BGR2GRAY)
        hst_im = cv2.cvtColor(org_im, cv2.COLOR_BGR2HSV)
        #hst_im = cv2.cvtColor(org_im, cv2.COLOR_BGR2GRAY)
        #hst_im = cv2.equalizeHist(gry_im)
        bkt1 = cv2.split(hst_im)
        cv2.equalizeHist(bkt1[2],bkt1[2])
        hst_im = cv2.merge((bkt1[0],bkt1[1],bkt1[2]))
        hst_im = cv2.cvtColor(hst_im, cv2.COLOR_HSV2BGR)
        hst_im = cv2.cvtColor(hst_im, cv2.COLOR_BGR2GRAY)
        ##
        
        #org_im = cv2.cvtColor(org_im, cv2.COLOR_RGB2BGR)
        
        bb = cv2.split(org_im)
        
        #bb = cv2.merge((bb[2],bb[1],bb[0]))
        
        hsv_im = cv2.cvtColor(org_im, cv2.COLOR_BGR2HSV)
        #hsv_im = cv2.cvtColor(hsv_im, cv2.COLOR_HSV2RGB)
        bkt2 = cv2.split(hsv_im)
        cv2.equalizeHist(bkt2[2],bkt2[2])
        skk_im = cv2.merge((bkt2[0],bkt2[1],bkt2[2]))
        skk_im = cv2.cvtColor(skk_im, cv2.COLOR_HSV2BGR)
        
        
        fushi1 = cascade.detectMultiScale(org_im, 1.1, 3) 
        fushi2 = cascade.detectMultiScale(skk_im, 1.1, 3) 
        fushi3 = cascade.detectMultiScale(gry_im, 1.1, 3) 
        fushi4 = cascade.detectMultiScale(hst_im, 1.1, 3) 
        #fushi5 = cascade.detectMultiScale(hsv_im, 1.1, 3) 
        
       
        for (x, y, w, h) in fushi1:
            print("%d,%d,%d,%d" %(x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(org_im, center, radius, cv.RGB(255, 0, 0), thickness=3) 
            
            
        for (x, y, w, h) in fushi2:
            print("%d,%d,%d,%d" %(x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(skk_im, center, radius, cv.RGB(255, 0, 0), thickness=3) 
            
        for (x, y, w, h) in fushi3:
            print("%d,%d,%d,%d" %(x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(gry_im, center, radius, cv.RGB(255, 255, 255), thickness=3)
             
        for (x, y, w, h) in fushi4:
            print("%d,%d,%d,%d" %(x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(hst_im, center, radius, cv.RGB(255, 255, 255), thickness=3) 
        """  
        for (x, y, w, h) in fushi5:
            print("%d,%d,%d,%d" %(x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(hsv_im, center, radius, cv.RGB(255, 255, 255), thickness=3)
        """

        #while(cap.isOpened())
        #if g_frame == None:
         #   break
        
        cv2.imshow('ORG', org_im)
        cv2.imshow('SKK', skk_im)
        cv2.imshow('GRY', gry_im)
        cv2.imshow('HST', hst_im)
       # cv2.imshow('HSV', hsv_im)
        
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
