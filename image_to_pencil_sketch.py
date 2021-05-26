import cv2
import sys
from speak1 import speak

speak("Enter the name of file with its location in proper address form: ")
add=input("Enter the name of file with its location in proper address form: ")
image=cv2.imread(add)
image=cv2.resize(image,(300,300))
#image.resize((300,300))
speak("Enter name of file you want to save with its format: ")
filename = input("Enter name of file you want to save with its format: ")
grayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
grayImageInv=255-grayImage
grayImageInv=cv2.GaussianBlur(grayImageInv,(21,21),0)
output=cv2.divide(grayImage,255-grayImageInv,scale=256.0)
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("pencilsketch",cv2.WINDOW_AUTOSIZE)
cv2.imshow("image",image)
cv2.imshow("pencilsketch",output)
cv2.imwrite(filename, output)

print("File saved")
speak("File created and saved")


cv2.waitKey(0)
cv2.destroyAllWindows()
