import cv2

# 最初の画像の左上の切り出しポイン
base_x = 190  #cols
base_y = 681  #rows

# 文字サイズ
width = 176
height = 176

# 1枚に記録されている文字の個数
row = 9
col = 12

y = base_y
for i in range(row):
    x = base_x
    for j in range(col):
        src = cv2.imread('../image/oeda1.jpg', 1)
        dst = src[y:y+height, x:x+width]
        cv2.imwrite('../result/' + str(i) + str(j) + '.jpg', dst)
        x = x + width + 3 
    y  = y + height + 129 # 124は縦の文字と文字間の距離
