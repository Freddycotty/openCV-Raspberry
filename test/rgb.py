import cv2
import numpy as np
bgr = cv2.imread('files/gti.jpeg')
C1 = bgr[:,:,0] 
C2 = bgr[:,:,1]
C3 = bgr[:,:,2]

cv2.imshow('BGR', np.hstack([C1, C2, C3]))
cv2.waitKey(0)
cv2.destroyAllWindows()