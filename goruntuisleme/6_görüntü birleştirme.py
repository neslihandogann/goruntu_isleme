import cv2
import numpy as np 

# resmi içe aktar 
img = cv2.imread("lenna.png",0)
#cv2.imshow("Orijinal", img)

# yatay
hor = np.hstack((img,img,img))
cv2.imshow("Yatay",hor)

# dikey
ver = np.vstack((hor,hor))
cv2.imshow("Dikey",ver)