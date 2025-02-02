
import cv2


#loads image
img = cv2.imread("goop.png")
assert img  is not None, "File is missing"

print(img) 

