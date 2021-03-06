# 画像からカスケード分類器を用いて顔認識を行うサンプル
 
import cv2
 
# サンプル顔認識特徴量ファイル
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
image_path = "image/Lenna.png"
 
# これは、BGRの順になっている気がする
color = (255, 255, 255) #白
 
# 画像の読み込み
image = cv2.imread(image_path)
# グレースケール変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# 分類器を作る?みたいな作業
cascade = cv2.CascadeClassifier(cascade_path)
 
# 顔認識の実行
facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
 
if len(facerect) > 0:
  # 検出した顔を囲む矩形の作成
  for rect in facerect:
    cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
else:
  print("no face")
 
# 認識結果の表示
cv2.imshow("detected.jpg", image)
 
# 何かキーが押されたら終了
while(1):
  if cv2.waitKey(10) > 0:
    break
