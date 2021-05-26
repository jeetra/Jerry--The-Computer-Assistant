import shutil
from os import path
from speak1 import speak
import os
import cv2
from datetime import datetime
os.system('python wait_2_sec.py')
speak("Kindly adjust yourself in the camera")
speak("Press S to capture the photo")
camera = cv2.VideoCapture(0)
today = datetime.now()
c=today.strftime(r"%d.%m.%Y-%H.%M.%S")#
cs=str(c)+'.jpg'
extension=".jpg"
file_name=cs+extension
print(cs)
print(file_name)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('d.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()
os.rename('d.jpg',cs)
#os.renames('d.jpg',file_name)
print("Photo Saved")
