import cv2
import matplotlib.pylab as plt
import sys

# OpenCV : 컴퓨터 비전 작업을 수행하기 위한 강력한 라이브러리

'''
cv2.imread(filename, flags) : 이미지 파일을 읽어서 OpenCV 이미지 객체로 반환함
           파일 경로를 입력으로 받아들이고, 이미지 데이터가 담긴 numpy 배열로 반환함

cv2.imshow(윈도우 창의 이름 , cv2.imread()함수로 읽어들인 이미지 ) : 이미지를 윈도우 창에 표시함
            이후 cv2.waitKey() 함수를 사용하지 않으면 윈도우가 바로 닫혀버림
'''

# BMP 파일을 불러와서 출력하는 소스 코드 추가 입력
print('Hello OpenCV',cv2.__version__)

# cat.bmp 파일을 불러와 img 변수에 저장
img = cv2.imread('cat.bmp')

# 영상 파일 불러오기가 실패하면 에러 메시지를 출력하고 종료
if img is None:
    print('Image load failed!')
    sys.exit()
    
# 'image'라는 이름의 새 창을 만들고, 이 창에 img 영상을 출력하고,
# 키보드 입력이 있을 때까지 대기
cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.waitKey()

# 생성된 모드 창을 닫음
cv2.destroyAllWindows()
    
