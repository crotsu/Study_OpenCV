import cv2
import numpy as np

for filenumber in range(108):
  filename = '../result/oeda_1_' + str(filenumber) + '.jpg'
  im = cv2.imread(filename, 0)
  kernel = np.zeros((5,5),np.uint8)
  im = cv2.dilate(im,kernel,iterations = 1)

  hight = im.shape[0]
  width = im.shape[1]
  half_size = cv2.resize(im, (28,28))

  newfilename = 'small' + str(filenumber) + '.jpg'
  cv2.imwrite(newfilename,half_size)