import cv2
import numpy as np

# 2枚の画像をグレースケールで取得
im1 = cv2.imread("source.jpg",0)
im2 = cv2.imread("target.jpg",0)

height = max(im1.shape[0], im2.shape[0])
width = max(im1.shape[1], im2.shape[1])

im1.resize(height, width)
im2.reshape(height, width)

# 画像データを重ねあわせ
im = im2

cv2.imshow("test",im)
cv2.waitKey(0)
cv2.destroyAllWindows()    # ウィンドウ破棄
