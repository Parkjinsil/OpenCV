import cv2

# 웹카메라 입력을 동영상으로 저장하기
cap = cv2.VideoCapture(0)

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
out = cv2.VideoWriter('output.avi',fourcc, 30, (w,h))

while True:
    ret, frame = cap.read()
    
    inversed = ~frame
    out.write(inversed)
    
    cv2.imshow('frame',frame)
    cv2.imshow('inversed',inversed)
    if cv2.waitKey(10) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()