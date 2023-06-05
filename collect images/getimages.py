import cv2
from datetime import datetime
import os
cap = cv2.VideoCapture(0)
num = 0
while cap.isOpened():
    succes, img = cap.read()
    img=cv2.resize(img,(128,128))   # change size of picture
    k = cv2.waitKey(2)
    if k == 0:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        myDirectory = os.path.join(os.getcwd(), 'images')
        now = datetime.now()
        timestamp = str(datetime.timestamp(now)).replace('.', '')
        #print("timestamp =", timestamp)
        fileName = os.path.join(myDirectory,f'Image_{timestamp}.jpg')
        cv2.imwrite(fileName, img)
        
        print("image saved!")
        num += 1
    cv2.imshow('Img',img)
    if cv2.waitKey(1) & 0xFF == ord(' '):   # Push the space bar and maintan to exit this Programm
        break 
cap.release()
cv2.destroyAllWindows()
