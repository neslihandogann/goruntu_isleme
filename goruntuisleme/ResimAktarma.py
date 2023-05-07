import cv2
import time

#resim aktarma
img=cv2.imread("evrim.jpg",0)

#resime ekrana bas
cv2.imshow("Flowers",img)

#ekrana gelen resmi istenilen tus ile kapama icin ascii kodu uretme
k=cv2.waitKey(0)
print(k)
#esc tusu ile kapa durumu
if k==27:
    cv2.destroyAllWindows()
#q tusu ile kapamak istersek
if k==ord('q'):
    #resimi kaydedip kapatmak istersek
    cv2.imwrite("evrim_gray.jpg", img)
    cv2.destroyAllWindows()







