import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
# cv2.imread() 함수로 불러온 영상의 색상 정보는 BGR순서이므로 이를 RGB순서로 변경해야함
# -> cv2.cvtColor() 함수
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
# plt.imshow() 함수에서 컬러맵을 cmap='gray'으로 지정
imgGray = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()