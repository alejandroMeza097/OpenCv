
#Aprendiendo sobre la interpretacion en la computadora de una imagen...
import cv2
import random
img = cv2.imread('video2\img\prague-july-14-bmw-r-260nw-454382617.jpg')
print(img.shape) #imprime las dimensiones del numpy array
print(type(img))#imprime numpy.ndarray

#cambiango algunos pixeles de forma aleatoria...
for i in range(150):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()