import sys
import cv2

# 기본 카메라 장치 열기
cap = cv2.VideoCapture(0)

while True:
    # 카메라로부터 프레임을 정상적으로 받아오면 ret에는 True, frame에는 해당 프레임이 저장됨
    ret ,frame = cap.read()
    
    # 현재 프레임 반전
    inversed = ~frame
    cv2.imshow('frame',frame)
    cv2.imshow('inversed',inversed)
    
    # 일정 시간(e.g. 10ms) 기다린 후 다음 프레임 처리. 만약 ESC 키를 누르면 while 루프 종료
    if cv2.waitKey(10) == 27:
        break
    
# 사용한 자원 해제
cap.release()
cv2.destroyAllWindows()

