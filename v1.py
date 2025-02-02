
import cv2

imagepath = "goop.png"


#loads image
img = cv2.imread(imagepath)
assert img  is not None, "File is missing"

print(img) 

