import cv2

# 
img = cv2.imread("evrim.jpg",0)
#print("Resim boyutu: ", img.shape)
#img[:100,:100]=0
#cv2.imshow("Orijinal", img)

# resized
imgResized = cv2.resize(img, (800,800))
#print("Resized Img Shape: ", imgResized.shape)
#cv2.imshow("Img Resized",imgResized)


# kırp
imgCropped = imgResized[100:200,200:300] # width height -> height width 
cv2.imshow("Kirpik Resim",imgCropped)