import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading image and its properties
img = cv2.imread('tiger.jpg')
img1 = cv2.imread('deer.jpg')


#print(img)
#print(img.shape)
#print(img.dtype)



#Displaying image
#cv2.imshow('Tiger', img)



#Converting image type
#cv2.imwrite('tiger1.png', img)




#Resizing image
resize = cv2.resize(img, (700,500))
resize1 = cv2.resize(img1, (700,500))
#cv2.imshow('resize', resize)
#cv2.imshow('resize1', resize1)




#Converting to B&W and Negative effect

baw = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Black&white', baw)



#Converting to Negative effect
negative = 1 - resize
#cv2.imshow('Negative', negative)




#Creating empty image
img1 = np.zeros((500,500,3), dtype=np.uint8)
#img1.fill(255) #Fill color by one argument
img1[:] = [137,167,255] #Fill color by three argument
#cv2.imshow('Image', img1)



#Writing text on images
text = cv2.putText(img1, "Mnv", (200,200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0,175, 0))
#cv2.imshow('Text', text)


#Displaying images with matplotlib
rgb = cv2.cvtColor(text, cv2.COLOR_BGR2RGB) #change the color
plt.imshow(rgb)
plt.imshow(text)
#plt.show()


rgb1 = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB) #change the color
plt.imshow(rgb1)
#plt.show()



#Splitting and merging image channels
b = resize[:,:,0]
g = resize[:,:,1]
r = resize[:,:,2]
#b,g,r = cv2.split(resize)
bgr = cv2.merge([r,g,b])
plt.imshow(bgr)
#plt.show()




#Combining two images
horizontal = cv2.hconcat([resize,resize1]) #horizontally
#cv2.imshow('horizontal', horizontal)
vertical = cv2.vconcat([resize, resize1]) #vertically
#cv2.imshow('vertical', vertical)



#Cropping images
cropped = resize1[68:458, 141:485] #using numpy
#plt.imshow(resize1)
#plt.show()
#cv2.imshow('resize1', resize1)



#p = cv2.selectROI(resize1)
#crop = resize1[p[1]:p[1]+p[3], p[0]:p[1]+p[2]]
#cv2.imshow('crop', crop)

#Rotating and flipping images
angle = cv2.ROTATE_90_CLOCKWISE
rotate = cv2.rotate(resize1, angle)
#cv2.imshow('rotate', rotate)
#cv2.imshow('resize1', resize1)

flip = cv2.flip(resize1, 1)
#cv2.imshow('resize1', resize1)
#cv2.imshow('flipped', flip)



#Adding borders to images
border = cv2.copyMakeBorder(resize1,20,20,20,20, cv2.BORDER_CONSTANT, value=(0,0,0))
#cv2.imshow('border', border)


#Blurring and smoothing images
avgblur = cv2.blur(resize1, (3,3))
gaussblur = cv2.GaussianBlur(resize1, (3,3), 0)
#cv2.imshow('avgblur', avgblur)
#cv2.imshow('gaussblue', gaussblur)


smooth = cv2.edgePreservingFilter(resize1, cv2.RECURS_FILTER, 60, 0.3)
#cv2.imshow('smooth', smooth)


#Sketch effect
pencil, color = cv2.pencilSketch(resize1, 200, 0.1, shade_factor=0.1)
#cv2.imshow('Pencil_sketch', pencil)
#cv2.imshow('color_sketch', color)

#Saturation
imghsv = cv2.cvtColor(resize1, cv2.COLOR_BGR2HSV).astype('float32')
h,s,v = cv2.split(imghsv)
s = s * 2
s = np.clip(s,0,255)
imghsv = cv2.merge([h,s,v])
saturated = cv2.cvtColor(imghsv.astype('uint8'), cv2.COLOR_HSV2BGR)
#cv2.imshow('Saturated', saturated)


#Brightness
alpha = 1 #alpha increases the brightness
beta = 50
adjusted = cv2.convertScaleAbs(resize1, alpha=alpha, beta=beta)
#cv2.imshow('adjusted', adjusted)


cv2.imshow('resize', resize1)
cv2.waitKey(2000)
cv2.destroyAllWindows()

