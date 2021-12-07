import cv2

image = cv2.imread('files/gti.jpeg', 0)
cv2.imshow('GTI - Desarrollo',image)
cv2.waitKey(2000)
cv2.imwrite('files/image(black_white).jpeg', image)
cv2.destroyAllWindows()