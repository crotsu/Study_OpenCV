import cv2
 
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

def detectFace(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.equalizeHist(image_gray)
 
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(50, 50))
 
    print("face rectangle")
    print(facerect)
 
    return facerect
 
 
### main ###
video_path = "oeda.mov" # 何かしらの動画ファイル。
cap = cv2.VideoCapture(video_path)
 
framenum = 0
faceframenum = 0
color = (255, 255, 255)
 
while(1):
    framenum += 1
 
    ret, image = cap.read()
    if not ret:
        break
 
    if framenum%10==0:
        facerect = detectFace(image)
        if len(facerect) == 0: continue
 
        for rect in facerect:
            croped = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            cv2.imwrite("detected" + str(faceframenum) + ".jpg", croped)
 
        faceframenum += 1
 
cap.release()
