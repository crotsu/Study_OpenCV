import cv2
import numpy as np

# 元画像
#img = cv2.imread('image/target8.jpg', 1)
img = cv2.imread('source.jpg', 1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二値変換
#thresh = 100
#max_pixel = 255
#ret, img = cv2.threshold(img,thresh,max_pixel,cv2.THRESH_TOZERO)

# テンプレート画像
template = cv2.imread('template/hoge10.png', 1)
#template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# 二値変換
#thresh = 100
#max_pixel = 255
#ret, template= cv2.threshold(template,thresh,max_pixel,cv2.THRESH_TOZERO)


# テンプレートマッチング
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
#res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
#res = cv2.matchTemplate(img,template,cv2.TM_CCORR_NORMED)

threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+30, pt[1]+30), (0,0,255), 2)
    
cv2.rectangle(img, (0,100), (200,200), (255,0,0, 2))

# width = 73
# height:
# 191:198
# 469:486
# 1605:1613
# sourceの座標を決定する
# 194, 481, 1609

width = []
height1 = []
height2 = []
height3 = []
for i in range(len(loc[0])):
    width.append(loc[1][i])
    if 170<loc[0][i] and loc[0][i]<220:
        height1.append(loc[0][i])
    elif 450<loc[0][i] and loc[0][i]<500:
        height2.append(loc[0][i])
    elif 1580<loc[0][i] and loc[0][i]<1630:
        height3.append(loc[0][i])


# 出力
cv2.imwrite('img.png',img)
cv2.imwrite('template.png',template)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
