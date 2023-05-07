import cv2
import numpy as np

# resim oluştur
#img=255 * np.ones((1000,1000,3), np.uint8)
#img =255* np.ones((512,512), np.uint8) # siyah bir resim
img = cv2.imread("evrim.jpg")
img=cv2.resize(img, (800,800))
print(img.shape)

#cv2.imshow("Siyah", img)

# çizgi
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (0,0), (800,800), (0,0,255), 30) # BGR = (0,255,0)
cv2.line(img, (0,800), (800,0), (0,0,255), 30) # BGR = (0,255,0)
#cv2.imshow("Cizgi", img)

# dikdörtgen
# (resim, başlangıç, bitiş, renk )
cv2.rectangle(img, (0,0), (256,256), (255,0,0),5)
cv2.rectangle(img, (100,100), (300,300), (255,0,0),5)
#cv2.imshow("Dikdortgen", img)

# çember
# (resim, merkez, yarı çap, renk)
cv2.circle(img, (300,300), 45, (0,0,255),5)
cv2.imshow("Cember", img)

# metin
# (resim, başlangıç noktası, font, kalınlığı, renk)
cv2.putText(img, "yusuf", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Metin", img)