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

pattern = {"red" : 20 , "green" : 35 , "blue" :12}

imagepath = "bigTest.jpg"

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
          listtest = []
          
          final.extend(cypher[" "])
          for j in i :
               final.extend(cypher[j]) #get's the number that represents each letter 
     

     


     return final



def get_image(imagepath):
    img = cv2.imread(imagepath)
    assert img is not None, "File is missing"
    return img

def encript(img):
        red = pattern["red"]
        green = pattern["green"]
        blue = pattern["blue"]
        message = getMessage()
        finalImg = img
        print(message)
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
                                   print("0")
                                   if isEven(pixel[0]) : #detects that pixel is even meaning  no changes need to be made 
                                        print("even 0")
                                        #access the red value
                                        wordcount = wordcount+1
                                   else : #detects pixel is odd so it changes  it to even to represent 0 
                                        print("odd 0")
                                        if pixel[0] == 255: # checks to make sure the number is not 255 which is the max value of an RGB value
                                             pixel[0] = pixel[0]-1 #just makes it -1 to make it even instead of odd.    
                                        else:
                                             pixel[0] = pixel[0]+1
                                        wordcount = wordcount+1
                              else : #if the pixel value will be odd
                                   print("1")
                                   if isEven(pixel[0]) :   #checks if the pixel is odd or even 
                                        print("even 1") #if it's even when add 1 so it's odd

                                        pixel[0] = pixel[0]+1
                                        
                                        wordcount = wordcount+1
                                   else : #if it is odd no change is made 
                                        print("odd 1")
                                        wordcount = wordcount+1
                         else : #if it's not time to change a pixel this repeats the cycle
                              redCount = redCount+1



                    elif greenCount>0:
                         if greenCount == green:
                         
                              greenCount = 0
                              blueCount = 1
                              if message[wordcount] == 0 : #if the pixel value will be even
                                   print("0")
                                   if isEven(pixel[1]) : #detects that pixel is even meaning  no changes need to be made 
                                        print("even 0")
                                        #access the red value
                                        wordcount = wordcount+1
                                   else : #detects pixel is odd so it changes  it to even to represent 0 
                                        print("odd 0")
                                        if pixel[1] == 255: # checks to make sure the number is not 255 which is the max value of an RGB value
                                             pixel[1] = pixel[1]-1 #just makes it -1 to make it even instead of odd.    
                                        else:
                                             pixel[1] = pixel[1]+1
                                        wordcount = wordcount+1
                              else : #if the pixel value will be odd
                                   print("1")
                                   if isEven(pixel[1]) :   #checks if the pixel is odd or even 
                                        print("even 1") #if it's even when add 1 so it's odd

                                        pixel[1] = pixel[1]+1
                                        
                                        wordcount = wordcount+1
                                   else : #if it is odd no change is made 
                                        print("odd 1")
                                        wordcount = wordcount+1
                         else:
                              greenCount = greenCount+1
                    elif blueCount>0:
                         if blueCount == blue:
                         
                              blueCount =0
                              redCount = 1
                              if message[wordcount] == 0 : #if the pixel value will be even
                                   print("0")
                                   if isEven(pixel[2]) : #detects that pixel is even meaning  no changes need to be made 
                                        print("even 0")
                                        #access the red value
                                        wordcount = wordcount+1
                                   else : #detects pixel is odd so it changes  it to even to represent 0 
                                        print("odd 0")
                                        if pixel[2] == 255: # checks to make sure the number is not 255 which is the max value of an RGB value
                                             pixel[2] = pixel[2]-1 #just makes it -1 to make it even instead of odd.    
                                        else:
                                             pixel[2] = pixel[2]+1
                                        wordcount = wordcount+1
                              else : #if the pixel value will be odd
                                   print("1")
                                   if isEven(pixel[2]) :   #checks if the pixel is odd or even 
                                        print("even 1") #if it's even when add 1 so it's odd

                                        pixel[2] = pixel[2]+1
                                        
                                        wordcount = wordcount+1
                                   else : #if it is odd no change is made 
                                        print("odd 1")
                                        wordcount = wordcount+1
                         else :
                              blueCount = blueCount+1
        except:
          cv2.imwrite("test.png",finalImg)


img = get_image(imagepath)





encript(img)

