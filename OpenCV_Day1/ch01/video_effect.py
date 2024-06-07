import cv2
import sys
import numpy as np
import os

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('C:/OpenCV/OpenCV_Day1/ch01/video1.mp4')
cap2 = cv2.VideoCapture('C:/OpenCV/OpenCV_Day1/ch01/video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed')
    sys.exit()
    
# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
# 비디오 파일의 프레임 속도(FPS: Frames Per Secound)를 가져옴
fps = cap1.get(cv2.CAP_PROP_FPS)
# 비디오의 프레임 속도를 이용하여 특정 효과를 적용할 프레임 수 계산
effect_frames = int(fps*2)

print('frame_cnt1 :',frame_cnt1)
print('frame_cnt2 :',frame_cnt2)
print('FPS : ',fps)

delay = int(1000/fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi',fourcc,fps,(w,h))

# 1번 동영상 복사
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()
    
    if not ret1:
        print('frame read error!')
        sys.exit()
        
    out.write(frame1)
    print('.',end='')
    
    cv2.imshow('output',frame1)
    cv2.waitKey(delay)
    
# 1번 동영상 뒷부분과 2번 동영상 앞부분 합성
for i in range(effect_frames):
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    
    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()
        
    dx = int(w / effect_frames)*i

    frame = np.zeros((h,w,3), dtype=np.uint8)
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :]
    
    out.write(frame)
    print(',',end='')
    
    cv2.imshow('output',frame)
    cv2.waitKey(delay)
    
# 2번 동영상 복사
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    if not ret2:
        print('frame2 read error!')
        sys.exit()
        
    out.write(frame2)
    print('.',end='')
    
    cv2.imshow('output',frame2)
    cv2.waitKey(delay)
    
print('\noutput.avi file is successfully generated!')

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
    


