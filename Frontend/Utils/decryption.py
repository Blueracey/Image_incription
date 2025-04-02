import cv2
from Utils.utils import is_even, to_char, get_message_length

# takes the image and interates through it following  the pattern provided to it 
# returns a list of  inveded lists where each list is 8 binary chreacter corosponding to an actual Character
def decript(img, pattern):
    messagelen = get_message_length(img) #get's the information it needs from the key
    red = pattern["red"]
    green = pattern["green"]
    blue = pattern["blue"]
    message = [] #empty list to append to 

    
    redCount = 1 #pattern starts with red so it starts with a value above 1 
    blueCount = 0
    greenCount = 0
    characterCount = 0



    

    
    for row in img: #row is the actual rows in the image 
            
            
            for pixel in row: #interates by each pixel so the pixel variable is an RGB value set
                    if characterCount == messagelen: 
                        break #breaks the loop so I don't repeat the patern until I am out of images
                    else:
                        if redCount>0: #if  red is above 0 it's the one  current set to be checked  
                            if redCount == red : # this detects if it's skipped enough pixels and its time to read one again 
                                
                                redCount = 0 
                                greenCount = 1 #changes green to be the next value to be checked 
                                characterCount = characterCount+1 #counts how many chracters have been added
                                if is_even(pixel[0]): #we already know  we are looking at the right pixel so this just checks if it's even 
                                        message.append(0) # if it's even it's a 0
                                else :
                                        message.append(1) #otherwise it's a 1 
                                
                            else : 
                                redCount = redCount+1 #if it's not the right pixel this continues the countdownm to the right one



                        elif greenCount>0: #if green is above 0 it's the one  current set to be checked  
                            if greenCount == green: # this detects if it's skipped enough pixels and its time to read one again 
                            
                                greenCount = 0
                                blueCount = 1 #changes blue to be the value being checked 
                                characterCount = characterCount+1 #counts how many chracters have been added
                                if is_even(pixel[1]): #we already know  we are lookjing at the right pixel so this just checks if it's even 
                                        message.append(0)# if it's even it's a 0
                                else :
                                        message.append(1)#otherwise it's a 1 
                                
                            else:
                                greenCount = greenCount+1 #if it's not the right pixel this continues the countdownm to the right one



                        elif blueCount>0: #if blue is above 0 it's the one  current set to be checked  
                            if blueCount == blue: # this detects if it's skipped enough pixels and its time to read one again 
                            
                                blueCount =0
                                redCount = 1 #changes red to the value being checked
                                characterCount = characterCount+1 #count how many chracters have been added
                                if is_even(pixel[2]):  #we already know  we are lookjing at the right pixel so this just checks if it's even 
                                        message.append(0) # if it's even it's a 0
                                else :
                                        message.append(1) #otherwise it's a 1 
                                
                            else :
                                blueCount = blueCount+1 #if it's not the right pixel this continues the countdownm to the right one

    
    return message 


def remakemessage(msg): #receives a embeded list of binary and converts it into a sentence 


    char = ""
    binary = []
    for i in msg: 

        char += str(i)
        if len(char) == 8:
            binary.append(char)
            char = ""

    
    


    final = "" #string that the loop below appends to

    for i in binary:
        
        final= final + str(to_char(i))





    return final 

    for row in range(rows):
        for col in range(cols):
            char_value = img[row, col, 0]  #Read from blue channel
            if char_value == 0:
                break
            decoded_message.append(chr(char_value))

    return ''.join(decoded_message)
