import cv2
import numpy as np

# 元画像
img = cv2.imread('../image/oeda1.jpg', 1)

# テンプレート画像
width = 50
height = 50
strokeWeight = 5
template = np.zeros((height, width, 3), np.uint8)
template[:,:] = [255, 255, 255]
# コーナーの横の直線
template[0:strokeWeight, :] = [0, 0, 0]
# コーナーの縦の直線
template[:, 0:strokeWeight] = [0, 0, 0]

# テンプレートマッチング
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)

# 出力
cv2.imwrite('corner.png',img)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
