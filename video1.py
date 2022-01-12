#introduction to open cv...
#importing open cv...
import cv2

#loading an image...
img = cv2.imread('video1/img/59d3b7763b5e88932e059cf281e7d48a.jpg',0)

#modificando las dimensiones..
width = int(img.shape[1]*(50/100))
height = int(img.shape[0]*(50/100))
dim = (width,height)
img = cv2.resize(img,dim)

#rotando imagen..
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

#guardando la imagen...
cv2.imwrite('rotate_img.jpg',img)

#displaying the image..
cv2.imshow("Techno",img)

#si no  se agrgan la siguientes lienas de codigo solo se ve un pantallazo de la imagen..
cv2.waitKey(0)
cv2.destroyAllWindows()
