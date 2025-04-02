import cv2
import random
from Utils.utils import get_image, get_message_bits, is_even


def isEven(val):
    return val % 2 == 0

def toBinary(char):
    return format(ord(char), '08b')

def encript(img, message, pattern):
    # takes the image and interates through it following  the pattern provided to it 
    # it then changes values by 1 in order to makie them positive or negative so we can later read that as binary 
    # it then saves the image and exits
    
    red = pattern["red"]
    green = pattern["green"]
    blue = pattern["blue"]
    message = get_message_bits(message) #get message returns a list of binary  values to put into the image
    FinalImg = img.copy()
    
    imageLen = len(message)
    redCount = 1
    blueCount = 0
    greenCount = 0
    wordcount = 0



    #the next 100 lines handle the hiding of the message lenght within the first pixel of the image    

    #it's also the worst code I have ever written 
    redimg = img[0][0][0]
    greenimg = img[0][0][1] 
    blueimg = img[0][0][2]

    firstDigitList = [] #collects the last digit of all the 
    #Num variables are the last Character of the RGB value
    for i in str(redimg):
        redNum = int(i)
    firstDigitList.append(redNum)
        
        
    for i in str(greenimg):
        greenNum = int(i)
    firstDigitList.append(greenNum)

        
        
    for i in str(blueimg):
        blueNum = int(i)
    firstDigitList.append(blueNum) 



    messageby8 = int(imageLen/8)
    messageby8ToStr = str(messageby8)
    if len(messageby8ToStr) == 3:
        pass
    elif len(messageby8ToStr) == 2 :
        messageby8ToStr = "0" +messageby8ToStr
    elif len(messageby8ToStr) == 1:

        messageby8ToStr = "00" +messageby8ToStr
    
    
    
    
    loopcount= 0
    for i,j in zip(messageby8ToStr,firstDigitList):
        
        if int(i) == j:
            pass
        elif int(i) < j :


            if int(i) == 0:

                    img[0][0][loopcount] = img[0][0][loopcount] - j

            else:
                    
                    dif =   j - int(i)
                    print(dif)
                    img[0][0][loopcount] = img[0][0][loopcount] - dif
        elif int(i) > j :
            dif = int(i)-j
            img[0][0][loopcount] = img[0][0][loopcount] + dif
        
        
        
        loopcount= loopcount+1
        
        
        





        


    #the following handles the  message incription itself 

    try :
        for row in img: #row is the actual rows in the image 
        


            for pixel in row: #interates by each pixel so the pixel variable is an RGB value set
                    
                    if redCount>0: #if this is higher the value we are  looking to change is red
                        if redCount == red : #if this is equal we've jumped the correct amount of pixels so it's time to change one
                            
                            redCount = 0 #sets red count to 0
                            greenCount = 1 #sets green count to one because it's the next number to be changed
                            

                            if message[wordcount] == 0 : #if the pixel value will be even
                            
                                if isEven(pixel[0]) : #detects that pixel is even meaning  no changes need to be made 
                                        
                                        #access the red value
                                        wordcount = wordcount+1
                                else : #detects pixel is odd so it changes  it to even to represent 0 
                                        
                                        if pixel[0] == 255: # checks to make sure the number is not 255 which is the max value of an RGB value
                                            pixel[0] = pixel[0]-1 #just makes it -1 to make it even instead of odd.    
                                        else:
                                            pixel[0] = pixel[0]+1
                                        wordcount = wordcount+1
                            else : #if the pixel value will be odd
                                
                                if isEven(pixel[0]) :   #checks if the pixel is odd or even 
                                        #if it's even when add 1 so it's odd

                                        pixel[0] = pixel[0]+1
                                        
                                        wordcount = wordcount+1
                                else : #if it is odd no change is made 
                                        
                                        wordcount = wordcount+1
                        else : #if it's not time to change a pixel this repeats the cycle
                            redCount = redCount+1



                    elif greenCount>0:
                        if greenCount == green:
                        
                            greenCount = 0
                            blueCount = 1
                            if message[wordcount] == 0 : #if the pixel value will be even
                                
                                if isEven(pixel[1]) : #detects that pixel is even meaning  no changes need to be made 
                                        
                                        #access the red value
                                        wordcount = wordcount+1
                                else : #detects pixel is odd so it changes  it to even to represent 0 
                                        
                                        if pixel[1] == 255: # checks to make sure the number is not 255 which is the max value of an RGB value
                                            pixel[1] = pixel[1]-1 #just makes it -1 to make it even instead of odd.    
                                        else:
                                            pixel[1] = pixel[1]+1
                                        wordcount = wordcount+1
                            else : #if the pixel value will be odd
                                
                                if isEven(pixel[1]) :   #checks if the pixel is odd or even 
                                        #if it's even when add 1 so it's odd

                                        pixel[1] = pixel[1]+1
                                        
                                        wordcount = wordcount+1
                                else : #if it is odd no change is made 
                                        
                                        wordcount = wordcount+1
                        else:
                            greenCount = greenCount+1
                    elif blueCount>0:
                        if blueCount == blue:
                        
                            blueCount =0
                            redCount = 1
                            if message[wordcount] == 0 : #if the pixel value will be even
                                
                                if isEven(pixel[2]) : #detects that pixel is even meaning  no changes need to be made 
                                        
                                        #access the red value
                                        wordcount = wordcount+1
                                else : #detects pixel is odd so it changes  it to even to represent 0 
                                        
                                        if pixel[2] == 255: # checks to make sure the number is not 255 which is the max value of an RGB value
                                            pixel[2] = pixel[2]-1 #just makes it -1 to make it even instead of odd.    
                                        else:
                                            pixel[2] = pixel[2]+1
                                        wordcount = wordcount+1
                            else : #if the pixel value will be odd
                                    
                                if isEven(pixel[2]) :   #checks if the pixel is odd or even 
                                        #if it's even when add 1 so it's odd

                                        pixel[2] = pixel[2]+1
                                        
                                        wordcount = wordcount+1
                                else : #if it is odd no change is made 
                                        
                                        wordcount = wordcount+1
                        else :
                            blueCount = blueCount+1
    except:
        cv2.imwrite("encrypted_output.png", img) # HIGHLIGHTED: Save to consistent output path
        print("Encription completed")


# img = get_image(imagepath)
