import cv2
import numpy as np

# 마스킹은 이전에 있던 이미지에 마스크를 씌우는 것임. 마스크를 씌운 영역만 화면에 보이는 것임.

print("OpenCV version: ")
print(cv2.__version__)

img = cv2.imread("/Users/hansohee/Desktop/Apple.png")
print("width: {} pixels".format(img.shape[1]))
print("height: {} pixels".format(img.shape[0]))
print("channels : {}".format(img.shape[2]))

(height, width) = img.shape[:2]
center = (width // 2, height // 2)

cv2.imshow("Apple", img)

# 이미지 마스킹 하는 방법
# mask = np.zeros(img.shape[:2], dtype = "uint8")  # img.shape[:2] 영역에 zero 값을 채워줌. zero 값은 rgb 0,0,0 즉, 검정색을 의미.
                                                # img.shape[:2]은 width와 height이므로 높이와 너비에 대한 영역을 검정색으로 마스킹.
#cv2.circle(mask, center, 300, (255, 255, 255), -1)  # mask -> 방금 만든 검은색 배경. / center -> 원의 중심. / 300 -> 크기 지정한 것. 마음대로 조정 가능. / -1 -> 두께. 전체가 채워짐.
#cv2.imshow("mask", mask)

# 위에서 만든 mask와 circle을 합쳐 보자. -> 이때 쓰는 bitwise 연산자.

#masked = cv2.bitwise_and(img, img, mask = mask)  # and는 공통적인 부분을 나타내어줌.

#cv2.imshow("Apple with mask", masked)
# 여기까지가 마스킹 하는 방법


# 채널 분해하는 방법
(Blue, Green, Red) = cv2.split(img)  # 이미지를 블루, 그린, 레드로 분해.

cv2.imshow("Red Channel", Red)
cv2.imshow("Green Channel", Green)
cv2.imshow("Blue Channel", Blue)
cv2.waitKey(0)

# 자신의 색상만 보이게 하는 방법
zeros = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, Red]))  # red
cv2.imshow("Green", cv2.merge([zeros, Green, zeros]))  # grreen
cv2.imshow("Blue", cv2.merge([Blue, zeros, zeros]))  # blue 색상만 보임.

# 필터
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # cv2의 COLOER BGR을 Gray로 변경
cv2.imshow("Gray Filter", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Filter", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB Filter", lab)

# 채널 더하기
BGR = cv2.merge([Blue, Green, Red])
cv2.imshow("Blue, Green and Red", BGR)

cv2.waitKey(0)
cv2.destroyAllWindows()
