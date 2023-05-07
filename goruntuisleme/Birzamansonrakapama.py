import cv2
import time

#resim aktarma
img=cv2.imread("evrim.jpg",1)

#resime ekrana bas
cv2.imshow("Flowers",img)
#ekranda bir zaman tutup kapatmak
initial_time = time.time()
#sifir olursa klavyeden giris yapana kadar bekler 
#eger sifirdan farkli ise girilen sure kadar bekler
cv2.waitKey(0)
final_time = time.time()
cv2.destroyAllWindows()
print("Window is closed after",(final_time-initial_time))