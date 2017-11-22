import cv2

img = cv2.imread('img/ingrid-color.jpg') #load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv

h, s, v = cv2.split(hsv)
v += 100
final_hsv = cv2.merge((h, s, v))

res = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('', res)
cv2.waitKey(0)