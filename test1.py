import  cv2.cv2 as cv2
import numpy as np

'''
img=np.random.randint(0,256,size=[256,256],dtype=np.uint8)
print("img=\n",img)
#print("读取像素点img.item(3,2)=",img.item(3,2))
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
img=cv2.imread("abc.jpg",0)
img.itemset((3,2),255)
cv2.imshow("before",img)
for i in range(10,100):
    for j in range(80,100):
        img.itemset((i,j),255)
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
img=np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
cv2.imshow("demo",img)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
im=cv2.imread("abc.jpg",-1)
a=im[0:720,0:500]
cv2.imshow("or",im)
cv2.imshow("ot",a)
cv2.waitKey()
cv2.destroyAllWindows()
'''
'''
a=cv2.imread("cc.jpg",-1)
cv2.imshow("before",a)
b,g,r=cv2.split(a)
#cv2.imshow("b",b)
#cv2.imshow("g",g)
#cv2.imshow("r",r)
brg=cv2.merge([b,r,g])
rgb=cv2.merge([r,g,b])
cv2.imshow("1号",brg)
cv2.imshow("2号",rgb)

cv2.waitKey()
cv2.destroyAllWindows()
'''
a=cv2.imread("cc.jpg",-1)
b=np.random.randint(0,256,size=[900,1200,3],dtype=np.uint8)
cv2.imshow("bbb",b)
c=cv2.add(a,b)
cv2.imshow("new",c)
cv2.waitKey()
cv2.destroyAllWindows()