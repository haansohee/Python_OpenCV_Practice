import cv2
import numpy as np

model_name = './model/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name = './model/deploy.prototxt.txt'
min_confidence = 0.3
file_name = "./image/marathon_01.jpg"

def detectAndDisplay(frame):  # 읽어온 이미지를 frame이라는 이름으로 받아 함수 내에서 사용.
    model = cv2.dnn.readNetFromCaffe(prototxt_name, model_name)  # model이라는 Caffe 모델 생성.

    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,  # cv2.dnn.bolbFromImage 함수로 모델에서 사용할 blob 이미지 생성.
            (300, 300), (104.0, 177.0, 123.0))  # image: 사용할 이미지를 지정.여기서는 모델에서 300x300 크기를 사용하므로 cv2.resize(frame, (300, 300))명령으로 크기를 이에 맞게 조정.
                                                #  scalefactor: 이미지의 크기 비율을 지정. 여기서는 1.0을 지정해 줬으므로 크기의 변형 없음.

                                                # size: Convolutional Netural Network에서 사용할 이미지 크기 지정. 300x300 사용함.
                                                # mean :Mean Subtraction 값을 RGB 색상 채널별로 지정해 주는 경험치 값. Mean Subtraction 값은 RGB 값의 일부를 제외해서 dnn이 분석하기 쉽게 단순화해 주는 값.
                                                # (104.0, 177.0, 123.0) 값은 경험치에서 나온 최적의 값으로 절대적인 수치는 아님.

    # 분석할 blob 이미지를 만들고나서, setInput과 forward 함수를 이용하여 결과값을 detections라는 배열에 저장한다.
    model.setInput(blob)
    detections = model.forward()

    # detections에 젖아된 결과값은 4차원 배열로 되어 있는데, 그 중 우리가 사용할 것은
    print(detections[0, 0])   # 처음에 있는 detections[0, 0] 값인 2차원 배열임.
    print(detections.shape[2])  # 200이 출력됨. detections.shape[2]은 이 모델이 갖고 올 수 있는 박스의 최대 크기.

    for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > min_confidence:
                    box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                    (startX, startY, endX, endY) = box.astype("int")
                    print(i, confidence,detections[0, 0, i, 3], startX, startY, endX, endY)
     
                    text = "{:.2f}%".format(confidence * 100)
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                            (0, 255, 0), 2)
                    cv2.putText(frame, text, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Face Detection by dnn", frame)
    
    
print("OpenCV version:")
print(cv2.__version__)
 
img = cv2.imread(file_name)
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels: {}".format(img.shape[2]))

(height, width) = img.shape[:2]

cv2.imshow("Original Image", img)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
