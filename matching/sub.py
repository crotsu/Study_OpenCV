import cv2
import numpy as np

# 2枚の画像をグレースケールで取得
im1 = cv2.imread("temp_source.png",0)
im2 = cv2.imread("temp_target.png",0)

height = max(im1.shape[0], im2.shape[0])
width = max(im1.shape[1], im2.shape[1])

pic1 = cv2.resize(im1, (height, width))
pic2 = cv2.resize(im2, (height, width))

dilation1 = cv2.dilate(pic1, np.ones((2,2)), iterations=1)
dilation2 = cv2.dilate(pic2, np.ones((2,2)), iterations=1)


# 画像データの引き算
pic = (dilation2 - dilation1)>100
pic = ~pic


cv2.imshow("test", pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
