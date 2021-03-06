import cv2 as cv
cascadeModel = cv.data.haarcascades + "haarcascade_frontalface_default.xml"
cascadeWajah = cv.CascadeClassifier(cascadeModel)

cam = cv.VideoCapture(0)

while True:
    sukses, video = cam.read()
    ubahKeGray = cv.cvtColor(video, cv.COLOR_BGR2GRAY)
    wajah = cascadeWajah.detectMultiScale(ubahKeGray,1.1,3)

    for (x, y, w, h) in wajah:
        blur = cv.GaussianBlur(video[y:y+h, x:x+w], (91,91),0)
        video [y:y+h, x:x+w] = blur

    cv.imshow('Blur Wajah', video)

    if cv.waitKey(1) & 0xff==ord('q'):
        break

cam.release()
cv.destroyAllWindows()