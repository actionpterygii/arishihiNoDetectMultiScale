# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 13:52:37 2016

@author: _
"""


import cv, cv2, numpy as np


if __name__ == '__main__':
    
    ESC_KEY = 27     
    INTERVAL= 33     
    FRAME_RATE = 30  

    DEVICE_ID = 0

    
    cap = cv2.VideoCapture(DEVICE_ID)

    
    end_flag, c_frame = cap.read()

    
    cascade = cv2.CascadeClassifier('scascade_shog.xml')
    
    rt,org_im = cap.read()

    
    while end_flag == True:
 
        rt,org_im = cap.read()
        
        height,width,chanels = org_im.shape
        ork_im = org_im[50:height,150:470]
        
        hsv_im = cv2.cvtColor(ork_im, cv2.COLOR_BGR2HSV)
        hsvbun = cv2.split(hsv_im)
        cv2.equalizeHist(hsvbun[2],hsvbun[2])
        skk_im = cv2.merge((hsvbun[0],hsvbun[1],hsvbun[2]))
        si_im = cv2.cvtColor(skk_im, cv2.COLOR_HSV2BGR)
       
        fushiii = cascade.detectMultiScale(ork_im, 1.1, 3) 
 
        i = 1
        for (x, y, w, h) in fushiii:
            print("%d,%d,%d,%d,%d" %(i, x, y, w, h))
            center = (int(x+w/2), int(y+h/2))
            radius = int(w/2+5)
            cv2.circle(ork_im, center, radius, cv.RGB(255, 255, 255), thickness=3)
            i += 1
         
        cv2.imshow('SKK', ork_im)
        
        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        c_frame = cap.read()
        
    cv2.destroyAllWindows()
    cap.release()
