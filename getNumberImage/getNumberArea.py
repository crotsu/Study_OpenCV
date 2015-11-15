# テンプレートマッチングを用いて，枠を検出する．
import cv2
import numpy as np
import pandas as pd

filenumber = 2

# 元画像 コーナーの数は16+12*9= 124
img = cv2.imread('../image/oeda' +str(filenumber) + '.jpg', 1)

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

# locをソートする
# 日付
sortVal = []
for (i, pt) in enumerate(zip(*loc[::-1])):
    if i<8:
        sortVal.append(pt)
    else:
        break
sortVal.sort()
corner.extend(sortVal)

# 名前
sortVal = []
for (i, pt) in enumerate(zip(*loc[::-1])):
    if 8<=i and i<16:
        sortVal.append(pt)
    elif 16<=i:
        break
sortVal.sort()
corner.extend(sortVal)

# 数字
sortVal = []
j = 0
for (i, pt) in enumerate(zip(*loc[::-1])):
    if 16<=i:
        sortVal.append(pt)
        j += 1
    if j==12:
        sortVal.sort()
        corner.extend(sortVal)
        sortVal = []
        j = 0

df = pd.read_csv('../numberSheet/rand' + str(filenumber) + '.csv', header=None)

# 枠領域を検出
size = corner[1][0] - corner[0][0]
for (i, pt) in enumerate(corner):
    cv2.rectangle(img, (pt[0]+3, pt[1]+3), (pt[0] + size-15, pt[1] + size-15), (255,255,255), 3)
    dst = img[(pt[1]+3):(pt[1]+size-15), (pt[0]+3):(pt[0]+size-15)]
    if i<8:
        filename = '../result/date' + str(i) + '.jpg'
    elif i<16:
        filename = '../result/name' + str(i-8) + '.jpg'
    else:
        filename = '../result/' + str(i-16) + '.jpg'

    cv2.imwrite(filename, dst)

# 教師信号を出力
f = open('teach.dat', 'w')
for col in range(12):
    for row in range(9):
        f.write(str(int(df[col][row]))+'\n')
f.close()

# 枠を出力
cv2.imwrite('corner.png',img)

