import cv2

import matplotlib as plt

def isEven(int):
    if (int%2)==0:
        return True
    else :
        return False



def saveAsText(image):
    with open("outputFile", "w") as out:
        for row in img: #row is the actual rows in the image 
            for pixel in row: #pixel is each individual pixel 
                if isEven(pixel[2]):
                    out.write(str(pixel[2]+1) + "\n")
                else:
                    out.write(str(pixel[2]) + "\n")


imagepath = "goop.png"

# Loads image
img = cv2.imread(imagepath)
assert img is not None, "File is missing"

print(img[0])

#img[0][0] = 63,92,12

img[0][0][0] = img[0][0][0]+1

print("_______")

print(img[0])


cv2.imwrite("test.png",img)

            
# looks promising https://www.geeksforgeeks.org/how-to-edit-a-pixel-value-using-opencv/