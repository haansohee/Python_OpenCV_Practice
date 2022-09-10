import cv2
import numpy as np

print("OpenCV Version: ")
print(cv2.__version__)

img = cv2.imread("/Users/hansohee/Desktop/Apple.png")  # 이미지를 가져올 때 shape라는 배열에 이미지의 높이, 너비, 채널 숫자를 넣어 가져 왔음.
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels : {}".format(img.shape[2]))

# shape배열에 저장된 값들을 아래에서 이미지 변형을 하면 여러번 쓰는데, 이 내용을 아래와 같이 변수에 넣어 활용할 수 있음. 

(height, width) = img.shape[:2]  # 이미지에서 shape 0번째 값을 height에, 1번째 값을 width 에 저장.
center = (width // 2, height // 2) # 나누기 2를 하여 center값 지정.

cv2.imshow("Apple", img)

# 상하, 좌우 대칭 하는 방법

flipped = cv2.flip(img, 1)  # 좌우대칭 : 1, 상하대칭 : 0, 좌우/상하 대칭 : -1
cv2.imshow("Flipped Horizontal 1, Vertical 0, both -1", flipped)

# 이미지 사이즈 변경하는 방법

# ratio = 200.0/ width  # 우리가 줄이고자 하는 가로 방향. 200 픽셀로 줄임.
# dimension = (200, int(height * ratio))  # 세로 방향.

# resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)  
# cv2.imshow("Resized", resized)

# 여기까지가 이미지 사이즈 변경하는 방법

# 이미지 돌리는 방법

# move = cv2.getRotationMatrix2D(center, 90, 1.0)  # 첫번째 파라미터 : 센터값, 두번째 파라미터 : 각도, 세번째 파라미터 : 스케일값.
# rotated = cv2.warpAffine(img, move, (width, height))  # 이미지, 로테이션 정보, 너비 높이 값 정보 넘겨주기.
# cv2.imshow("Rotated clockwise degress", rotated)

# 여기까지가 이미지 돌리는 방법

# 이미지 이동시키는 방법

# move = np.float32([[1, 0, 100], [0, 1, 100]])  # np(numpy)를 이용. 첫번째 배열에 있는 1과 0은 down과 up. 100이니까 양수이므로 100만큼 down.
                                                #음수일 경우 up.
                                                # 두번째 배열에 있는 0과 1은 오른쪽, 왼쪽. 100이 양수 값이면 수만큼 right측으로 이동.
# moved = cv2.warpAffine(img, move, (width, height))  # warpAffine func 이용.

# cv2.imshow("Moved down: +, up: - and right: +, left: -", moved)

# 여기까지가 이미지 이동시키는 방법 

# 이미지 위에 픽셀 단위로 사각형, 삼각형, 일직선, 텍스트 그리는 방법

#(b, g, r) = img[0, 0]  # 픽셀단위로 색 지정
#print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# dot = img[50:100, 50:100]  # 어디서부터 어디까지 갖고 옴

# img[50:100, 100:50] = (0, 0, 255)

#cv2.rectangle(img, (150, 50), (200, 100), (0, 255, 0), 5)
#cv2.circle(img, (275,75), 25, (0, 255, 255), -1)
#cv2.line(img, (350, 100), (400, 100), (255, 0, 0,), 5)
#cv2.putText(img, 'creApple', (450, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4)

#cv2.imshow("Apple - draw", img)

# 여기까지가 도형 그리는 방법

cv2.waitKey(0)
cv2.destroyAllWindows()
