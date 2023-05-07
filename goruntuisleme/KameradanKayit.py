import cv2
import time


#video yukleme
cap=cv2.VideoCapture(0)


#Kamera cozunurlugunu verir
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width," ",height)

#video kayit yeri fourcc cerceveleri birlestirmek icin kullnilan kodek kodu vindows icin
#fps=20 ve yukseklik genislik
#isColor=False gri kayit ve cv2.COLOR_BGR2GRAY
#isColor=True renkli kayit ve cv2.COLOR_BGR2GRAY kapanacak
wr=cv2.VideoWriter("Kayit.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height ),isColor=True)

#video hem gosterilecek ve kayit edilecek

ct=10;
x=50
y=50
while True:
    ref,frame=cap.read()
   # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #video renk degistirme
    cv2.circle(frame, (x,400), 50,(255,255,255))
    cv2.circle(frame, (400,y), 50,(0,0,0))
    cv2.imshow("video", frame)
    #kayit
    wr.write(frame)
    if cv2.waitKey(1)==ord('q'):
        break
    if x==width-50 or y==height-50:
        ct=ct*-1
    if x==0 or y==0:
        ct=10
    print(x)
    x=x+ct
    y=y+ct
cap.release()
wr.release()
cv2.destroyAllWindows()







