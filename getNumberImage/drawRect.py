import cv2
import numpy as np

img = cv2.imread('../image/oeda1.jpg', 1)

# テンプレート画像
cols = 30
rows = 30
template = np.zeros((rows, cols, 3), np.uint8)
#template[:,:] = [255, 255, 255]
template[3:,3:] = [255, 255, 255]


res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + cols, pt[1] + rows), (0,0,255), 2)

cv2.imwrite('corner.png',img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
