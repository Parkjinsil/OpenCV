import cv2
import sys
# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp',cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png',cv2.IMREAD_UNCHANGED)

if src  is None or logo is None:
    print('Image load failed')
    sys.exit()
    
mask = logo[:,:,3] # 0:B 1:G 2: R 3: Alpha
logo2 = logo[:,:,:-1] # 0, 1, 2 BGR
h,w = mask.shape[:2] # (height, width, 4): 2
crop = src[10:10+h,10:10+w]

cv2.copyTo(logo2,mask,crop)

cv2.imshow('src',src)
# cv2.imshow('logo',logo)
# cv2.imshow('mask',mask)
# cv2.imshow('crop',crop)
cv2.waitKey()
cv2.destroyAllWindows()

