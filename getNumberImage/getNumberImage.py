import cv2

x = 187  #cols
y = 678  #rows

width = 180
height = 180

num = 12

for i in range(num):
    src = cv2.imread('../image/oeda1.jpg', 1)
    dst = src[y:y+height, x:x+width]
    cv2.imwrite(str(i) + '.jpg', dst)
    x += width
