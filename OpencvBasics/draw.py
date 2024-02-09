import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

cv.rectangle(blank, (0,0),(300,200), (0,255,0),thickness= 1)
# cv.imshow("Rectangled blank",blank)
cv.circle(blank, (255,255), 40, (255,0,0), thickness=3)
cv.line(blank, (0,0), (255,255), (255,255,255), thickness= 2)
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow("edited blank", blank)
cv.waitKey(0)