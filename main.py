import cv2.cv2 as cv2
import  numpy as np
'''
img=np.zeros((8,8),dtype=np.uint8)
print("img=\n",img)
cv2.imshow("one",img)
print("读取像素点img[0,3]=",img[0,3])
img[0,3]=255
print("修改后img=\n",img)
print("读取修改后像素点img[0,3]=",img[0,3])
cv2.imshow("two",img)
cv2.waitKey()
lena = cv2.imread("abc.jpg")
cv2.imshow("demo", lena)

key = cv2.waitKey()
if key == ord('A'):
    cv2.imshow("PressA", lena)
elif key == ord('B'):
    cv2.imshow("PressB", lena)

img = cv2.imread("abc.jpg", 0)
cv2.imshow("before", img)
for i in range(10, 100):
    for j in range(80, 100):
        img[i, j] = 255
cv2.imshow("after", img)
cv2.waitKey()
cv2.destroyAllWindows() 

blue=np.zeros((300,300,3),dtype=np.uint8)
blue[:,:,0]=255
print("blue=\n",blue)
cv2.imshow("blue",blue)
#------------------------------------
green=np.zeros((300,300,3),dtype=np.uint8)
green[:,:,1]=255
print("green=\n",green)
cv2.imshow("green",green)
#------------------------------------
red=np.zeros((300,300,3),dtype=np.uint8)
red[:,:,2]=255
print("red=\n",red)
cv2.imshow("red",red)
#------------------------------------
cv2.waitKey()
cv2.destroyAllWindows()

img=np.zeros((300,300,3),dtype=np.uint8)
img[:,0:100,0]=255
img[:,100:200,1]=255
img[:,200:300,2]=255
print("img=\n",img)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
abc=cv2.imread("abc.jpg")
cv2.imshow("before",abc)
for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            abc[i,j,k]=255

for i in range(50,100):
    for j in range(0,100):
        for k in range(0,3):
            abc[i,j,k]=128

for i in range(100,150):
    for j in range(0,100):
        abc[i,j]=0

cv2.imshow("after",abc)
cv2.waitKey()
cv2.destroyAllWindows()
'''
img=cv2.imread("abc.jpg")
cv2.imshow("before",img)
cv2.waitKey()
cv2.destroyWindow("before")



