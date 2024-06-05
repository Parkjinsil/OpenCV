import cv2
src = cv2.imread('airplane.bmp',cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp',cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp',cv2.IMREAD_COLOR)
cv2.copyTo(src, mask, dst)

'''
cv2.copyTo(src,mask,dst=None)-> dst
src : 입력 영상
mask : 마스크 영상. cv2.CV_8U.(numpy.uint8)
       0이 아닌 픽셀에 대해서만 복사 연산을 수행
dst : 출력 영상. 만약 src와 크기 및 타입이 같은 dst를 입력으로 지정하면
      dst를 새로 생성하지 않고 연산을 수행
      그렇지 않으면 dst를 새로 생성하여 연산으르 수행한 후 반환함
'''

cv2.namedWindow('src')
cv2.namedWindow('mask')
cv2.namedWindow('dst')
cv2.imshow('src',src)
cv2.imshow('mask',mask)
cv2.imshow('dst',dst)
cv2.waitKey()

