import cv2
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
plt.figure(figsize=(20,20))

for i in range(1,4):
    #img = cv2.imread("/Users/YM/Desktop/mri"+str(i)+".png",0)
    img = cv2.imread("a.png")
    
    plt.subplot(4, 3, i)
    plt.imshow(img,clim=[0,255])
    plt.colorbar()
    plt.subplot(4, 3, i+3)
    plt.imshow(cv2.cvtColor(img.astype(np.uint8),cv2.COLOR_GRAY2BGR))
    plt.colorbar()
    
    print np.mean(img),np.std(img)
    img = (img - np.mean(img))/np.std(img)*16+64
    
    plt.subplot(4, 3, i+6)
    plt.imshow(img,clim=[0,255])
    plt.colorbar()
    plt.subplot(4, 3, i+9)
    plt.imshow(cv2.cvtColor(img.astype(np.uint8),cv2.COLOR_GRAY2BGR))
    plt.colorbar()
