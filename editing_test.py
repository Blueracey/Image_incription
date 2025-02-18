import cv2

def isEven(int):
    if (int%2)==0:
        return True
    else :
        return False

print(isEven(100))


imagepath = "goop.png"

# Loads image
img = cv2.imread(imagepath)
assert img is not None, "File is missing"

# Open output file
#with open("outputFile", "w") as out:
 #   for row in img: #row is the actual rows in the image 
 #       for pixel in row: #pixel is each individual pixel 
 #           out.write(str(pixel) + "\n")
            