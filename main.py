#   Project Image Resizer

import cv2

image = cv2.imread("thankyou.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("titile",image)

scale_percent = 50

width = int(image.shape[1]*scale_percent / 100)
height = int(image.shape[0]*scale_percent / 100)

dsize =(width,height)

output = cv2.resize(image,dsize)
output_path = r'C:\Users\rgrat\Downloads\DCSP\Python\Image_Resizer\resize_thankyou.jpg'
cv2.imwrite(output_path,output)
cv2.waitKey(0)
