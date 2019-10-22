# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 20:35:18 2016

@author: _
"""

# coding:utf-8
#!/usr/bin/env python
import cv, cv2

tar = 'sample.jpg'
im = cv2.imread(tar)
cascade = cv2.CascadeClassifier('cascade_hog.xml')
faces = cascade.detectMultiScale(im, 1.1, 3) 

for (x, y, w, h) in faces:
    print x, y, w, h
    center = (int(x+w/2), int(y+h/2))
    radius = int(w/2+5)
    cv2.circle(im, center, radius, cv.RGB(255, 0, 0), thickness=20) 

cv2.imwrite('result.jpg', im)