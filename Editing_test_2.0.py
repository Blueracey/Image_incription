#this is an atempt to use a dictionary to make a cypher 
import cv2


#the max value of RGB is 255,255,255 


cypher =  { "a":[0,1,1,0,0,0,0,1]
           ,"b":[0,1,1,0,0,0,1,0]
           ,"c" :[0,1,1,0,0,0,1,1]
           ,"d" :[0,1,1,0,0,1,0,0]
           ,"e" :[0,1,1,0,0,1,0,1]
           ,"f" :[0,1,1,0,0,1,1,0]
           ,"g" :[0,1,1,0,0,1,1,1]
           ,"h" :[0,1,1,0,1,0,0,0]
           ,"i" :[0,1,1,0,1,0,0,1]
           ,"j" :[0,1,1,0,1,0,1,0]
           ,"k" :[0,1,1,0,1,0,1,1]
           ,"l" :[0,1,1,0,1,1,0,0]
           ,"m" :[0,1,1,0,1,1,0,1]
           ,"n" :[0,1,1,0,1,1,1,0]
           ,"o" :[0,1,1,0,1,1,1,1]
           ,"p" :[0,1,1,1,0,0,0,0]

           ,"q" :[0,1,1,1,0,0,0,1]
           ,"r" :[0,1,1,1,0,0,1,0]
           ,"s" :[0,1,1,1,0,0,1,1]
           ,"t" :[0,1,1,1,0,1,0,0]
           ,"u" :[0,1,1,1,0,1,0,1]
           ,"v" :[0,1,1,1,0,1,1,0]
           ,"w" :[0,1,1,1,0,1,1,1]
           ,"x" :[0,1,1,1,1,0,0,0]
           ,"y" :[0,1,1,1,1,0,0,1]
           ,"z" :[0,1,1,1,1,0,1,0]
           ," " :[0,0,1,0,0,0,0,0]
             }

pattern = {"red" : 20 , "green" : 35 , "blue" :12, "length" : 120}

imagepath = "goop.png"

def isEven(int):
    if (int%2)==0:
        return True
    else :
        return False



def getMessage():
     message  = "Hi I am Corbyn" 
     split = message.split()


     finalletters = []
     
     for i in split: #seperates all the character and puts each word in it's own list within the main list
          finalletters.append(list(i.lower()))
     
     final = [] 
     for i in finalletters:

          
          final.extend(cypher[" "]) #adds a space 
          for j in i :
               final.extend(cypher[j]) #get's the number that represents each letter 
     

     


     return final



def get_image(imagepath):
    img = cv2.imread(imagepath)
    assert img is not None, "File is missing"
    return img





 
def encript(img):
     # takes the image and interates through it following  the pattern provided to it 
     # it then changes values by 1 in order to makie them positive or negative so we can later read taht as binary 
     # it then saves the image and exits

        red = pattern["red"]
        green = pattern["green"]
        blue = pattern["blue"]
        message = getMessage() #get message returns a list of binary  values to put into the image
        finalImg = img

        redCount = 1
        blueCount = 0
        greenCount = 0
        wordcount = 0
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
          cv2.imwrite("test.png",finalImg)
          print("Encription completed")


img = get_image(imagepath)



 # takes the image and interates through it following  the pattern provided to it 
 #returns a list of  inveded lists where each list is 8 binary chreacter corosponding to an actual Character
def decript(img):
     messagelen = pattern["length"]  #get's the information it needs from the key
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
                                   if isEven(pixel[0]): #we already know  we are lookjing at the right pixel so this just checks if it's even 
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
                                   if isEven(pixel[1]): #we already know  we are lookjing at the right pixel so this just checks if it's even 
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
                                   if isEven(pixel[2]):  #we already know  we are lookjing at the right pixel so this just checks if it's even 
                                        message.append(0) # if it's even it's a 0
                                   else :
                                        message.append(1) #otherwise it's a 1 
                                   
                              else :
                                   blueCount = blueCount+1 #if it's not the right pixel this continues the countdownm to the right one

     
     return message 


def remakemessage(msg): #receives a embeded list of binary and converts it into a sentence 
     count = 0
     character = []
     total = []

     c = 0
     for i in msg:

          
          if count == 7 :
               character.append(i)
               total.append(character)
               count = 0
               c = c+1
               character = []
          else :
               count = count +1
               character.append(i)

     
     final = "" #string that the loop below appends to


     for i in total: #loops trhough each list of binary
          for letter,binary in cypher.items(): #loops through the cypher and checks if the currently selected binary matches
               if i == binary :
                    final = final + letter #appends it to the string

     
     return final 





          




encript(img)


decriptimg = get_image("test.png")

message = decript(decriptimg)



print(remakemessage(message))



