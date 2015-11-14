# テンプレートマッチングを用いて，枠を検出する．
import cv2
import numpy as np

# 元画像 コーナーの数は16+12*9= 124
img = cv2.imread('../image/oeda1.jpg', 1)

# テンプレート画像
width = 50
height = 50
strokeWeight = 2
template = np.zeros((height, width, 3), np.uint8)
template[:,:] = [255, 255, 255]
# コーナーの横の直線
template[0:strokeWeight, :] = [0, 0, 0]
# コーナーの縦の直線
template[:, 0:strokeWeight] = [0, 0, 0]

# テンプレートマッチング 1回目
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
canvas = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
canvas[:,:] = [255, 255, 255]
for pt in zip(*loc[::-1]):
    cv2.rectangle(canvas, pt, (pt[0] + width*2, pt[1] + height*2), (0,0,0), 10)

# テンプレートマッチング2回目
res = cv2.matchTemplate(canvas,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
corner = []
for pt in zip(*loc[::-1]):
    corner.append(pt)

# 枠領域を検出
size = corner[1][0] - corner[0][0]
for (i, pt) in enumerate(corner):
    cv2.rectangle(img, (pt[0]+3, pt[1]+3), (pt[0] + size-15, pt[1] + size-15), (0,0,255), 3)
    dst = img[(pt[1]+3):(pt[1]+size-15), (pt[0]+3):(pt[0]+size-15)]
    cv2.imwrite('../result/' + str(i) + '.jpg', dst)

# 出力
cv2.imwrite('corner.png',img)

