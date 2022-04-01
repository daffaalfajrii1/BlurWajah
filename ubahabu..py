import cv2 as cv

img = cv.imread('FF.jpg')
img = cv.resize(img,(720,660))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("hasil ubah", gray)

cv.waitKey(0)