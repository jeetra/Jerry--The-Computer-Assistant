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

'''
import scipy.ndimageblur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=5)
def dodge(front,back): result=front*255/(255-back)  result[result>255]=255 result[back==255]=255 return result.astype(‘uint8’)
final_img= dodge(blur_img,gray_img)
import matplotlib.pyplot as pltplt.imshow(final_img, cmap=”gray”)
plt.imsave(‘img2.png’, final_img, cmap=’gray’, vmin=0, vmax=255)
''''''
import cv2
image=cv2.imread("C:\\Users\\Jeet Raiwal\\Pictures\\Camera Roll\\IMG-20190628-WA0011.jpg")
start_img.shape(196, 160, 30)
#Y= 0.299 R + 0.587 G + 0.114 B
import numpy as npdef 
grayscale(rgb):return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])
gray_img = grayscale(start_img)
inverted_img = 255-gray_img
import scipy.ndimageblur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=5)
def dodge(front,back): result=front*255/(255-back)  result[result>255]=255 result[back==255]=255 return result.astype(‘uint8’)
final_img= dodge(blur_img,gray_img)
import matplotlib.pyplot as pltplt.imshow(final_img, cmap=”gray”)
plt.imsave(‘img2.png’, final_img, cmap=’gray’, vmin=0, vmax=255)
'''
