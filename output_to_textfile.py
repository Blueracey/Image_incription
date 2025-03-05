import cv2



imagepath = "goop.png"

# Loads image
img = cv2.imread(imagepath)
assert img is not None, "File is missing"

# Open output file
with open("outputFile", "w") as out:
    for row in img: #row is the actual rows in the image 
        #out.write(str(row) + "\n")
        for pixel in row: #pixel is each individual pixel 
            out.write(str(pixel) + "\n")
            




#https://github.com/skxmxm/encrypt_in_image 
#https://www.geeksforgeeks.org/image-steganography-using-opencv-in-python/ 
# https://dev.to/erikwhiting88/let-s-hide-a-secret-message-in-an-image-with-python-and-opencv-1jf5 