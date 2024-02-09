import cv2 as cv

img = cv.imread('photos/cat.jpg')
def rescaleFrame(frame, scale = 0.2):
    # For imgs, videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] *scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


def changeRes(width, height):
    # Only For live videos
    capture.set(3, width)
    capture.set(4, height)

img2 = rescaleFrame(img)
cv.imshow("Reszied image",img2)

cv.waitKey(5000)
cv.destroyAllWindows()
#
capture = cv.VideoCapture('videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video-resized', resized_frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()