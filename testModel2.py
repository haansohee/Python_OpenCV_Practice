import cv2
import tensorflow
from keras.models import load_model
import numpy as np

# 이미지 전처리
def preprocessing(frame) :
    # 사이즈 조정
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)

    # 이미지 정규화
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

    # 이미지 차원 재조정 : 예측을 위해 reshape 해 줌.
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))

    return frame_reshaped

# 학습된 모델 불러오기
model_filename = 'test_model.h5'
model = load_model(model_filename, compile=False)

# 카메라 캡처 객체 0 -> 내장카메라
capture = cv2.VideoCapture(0)

# 캡쳐 프레임 사이즈 조절
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

while True :

    ret, frame = capture.read()
    frame_fliped = cv2.flip(frame, 1)

    if cv2.waitKey(200) > 0 :
        break

    preprocessed = preprocessing(frame_fliped)

    prediction = model.predict(preprocessed)

    if prediction[0, 1] < prediction[0, 0] and prediction[0, 2] < prediction[0, 0] :
        cv2.putText(frame_fliped, 'sohee', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    elif prediction[0, 0] < prediction[0, 1] and prediction[0, 2] < prediction[0, 1] :
        cv2.putText(frame_fliped, 'sehyeon', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    elif prediction[0, 0] < prediction[0, 2] and prediction[0, 1] < prediction[0,2] :
        cv2.putText(frame_fliped, 'insoo', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    else :
        cv2.putText(frame_fliped, 'Ex', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    cv2.imshow("Test", frame_fliped)

capture.release()
cv2.destroyAllWindows()