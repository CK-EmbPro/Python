import cv2 as cv

#
# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img)
#
# cv.waitKey(0)

capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.putText(frame, "hello dog", (0,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 1)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

