import cv2
cap = cv2.VideoCapture(0)
while (True):
    ret,frame = cap.read()
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(width)
    print(height)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# after reading the video it is important to release the captured video
cap.release()
cv2.destroyAllWindows()
