import cv2
import numpy as np

cv2.namedWindow("test")
cap=cv2.VideoCapture(0)
success,frame=cap.read()

classifier=cv2.CascadeClassifier("C:\\Program Files\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt.xml")

while success:
    success,frame=cap.read()
    size=frame.shape[:2]
    image=np.zeros(size,dtype=np.float16)
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(image,image)
    divisor=8
    h,w=size
    minSize=(int(w/divisor),int(h/divisor))
    faceRects=classifier.detectMultiScale(image,1.2,2,cv2.CASCADE_SCALE_IMAGE,minSize)
    if len(faceRects)> 0:
        for faceRect in faceRects:
            x,y,w,h=faceRect
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)
            cv2.circle(frame,(int(x+w/2),int(y+h/2)),min(int(w/2),int(h/2)),(255,0,0))
            cv2.circle(frame,(int(x+w/4),int(y+h/4)),min(int(w/8),int(h/8)),(255,0,0))
            cv2.circle(frame,(int(x+3*w/4),int(y+h/4)),min(int(w/8),int(h/8)),(255,0,0))
            cv2.rectangle(frame,(int(x+3*w/4),int(y+3*h/4)),(int(x+5*w/8),int(y+7*h/8)),(255,0,0))
    cv2.imshow("test",frame)
    key=cv2.waitKey(10)
    c=chr(key&255)
    if c in ['q','Q',chr(27)]:
        break
    # cv2.destroyWindow("test")
