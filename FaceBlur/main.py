import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector = FaceDetector(minDetectionCon=0.75)

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img,draw=False)

    if bboxs:
        for i,bbox in enumerate(bboxs):
            x,y,w,h = bbox['bbox']
            if x<0: x=0
            if y<0: y=0

            imgCrop = img[y:y +h, x:x+w]
            imgBlur = cv2.blur(imgCrop,(35,35))
            img[y:y+h,x:x+w] = imgBlur
            #cv2.imshow(f"cropped image {i}", imgcrop)

    cv2.imshow("Image",img)
    cv2.waitKey(1)