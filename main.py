import cv2 as cv
import numpy as np

def empty(a):
    pass
cv.namedWindow("HSV")
cv.resizeWindow("HSV",300,300)
cv.createTrackbar("HMin","HSV",0,255,empty)
cv.createTrackbar("HMax","HSV",255,255,empty)
cv.createTrackbar("SMin","HSV",0,255,empty)
cv.createTrackbar("SMax","HSV",255,255,empty)
cv.createTrackbar("VMin","HSV",0,255,empty)
cv.createTrackbar("VMax","HSV",255,255,empty)


v=cv.VideoCapture(0)
while True:
    ret,image=v.read()
    image_hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)


    h_min = cv.getTrackbarPos("HMin", "HSV")
    h_max = cv.getTrackbarPos("HMax", "HSV")
    s_min = cv.getTrackbarPos("SMin", "HSV")
    s_max = cv.getTrackbarPos("SMax", "HSV")
    v_min = cv.getTrackbarPos("VMin", "HSV")
    v_max = cv.getTrackbarPos("VMax", "HSV")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv.inRange(image_hsv,lower,upper)
    contours, hierarchy = cv.findContours(mask, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
    cv.drawContours(mask, contours, -1, (0, 255, 0), 3);


    Segmentation=cv.bitwise_and(image,image,mask=mask)
    cv.imshow("hello",Segmentation)
    cv.imshow("contours",mask )
    if cv.waitKey(50)&0xFF==ord("q"):
        break
