import matplotlib.pyplot as plt
import cv2

# Matplotlib을 이용하여 창 하나에 여러 개의 이미지 출력하기
# 컬러 영상 & 그레이스케일 영상 불러오기
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)
# 귀찮지만 이렇게 다 바꿔서 matplotlib 쓰는 이유 : 한 창에 여러개 띄울 수 있으니까

# 두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'),plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'),plt.imshow(imgGray,cmap='gray')
plt.show()