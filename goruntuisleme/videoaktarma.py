import cv2
import time


#video yukleme
cap=cv2.VideoCapture('1.MP4')

#frame sayisi hesapliyor
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)

#videonun cozunurlugunu verir
print("Genislik: ",cap.get(3))
print("Yukseklik: ",cap.get(4))


#video Acilip acilmadigini gosteriyor
if cap.isOpened()==False:
    print("Calismiyor")


#video icin frameleri yaratiyoruz ret islemin basarili olup olmadigini
#gosteriyor
frameNr = 0
while True:
    ret, frame=cap.read()
    if ret==True:
        time.sleep(0.01) # kullanmaksak cok hizli akar
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #video renk degistirme
        cv2.imwrite('dosya\\frame%d.png' %frameNr, gray)

        cv2.imshow("video",gray) #gri halde gosterme
    else: break
    if cv2.waitKey(1)==27:
        break
    frameNr = frameNr+1

#stop capture
cap.release() 
# tum pencereli kapa
cv2.destroyAllWindows() 






