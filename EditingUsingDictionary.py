def getMessage():
     message  = "Hi I am Corbyn" 
     split = message.split()


     finalletters = []
     
     for i in split: #seperates all the character and puts each word in it's own list within the main list
          finalletters.append(list(i.lower()))
     
     final = []
     for i in finalletters:
          listtest = []
          final.append(listtest)
          for j in i :
               listtest.append(cypher[j]) #get's the number that represents each letter 
     




     return final

cypher =  { "a": {}
           ,"b":2
           ,"c" :3
           ,"d" :4
           ,"e" :5
           ,"f" :6
           ,"g" :7
           ,"h" :8
           ,"i" :9
           ,"j" :10
           ,"k" :11
           ,"l" :12
           ,"m" :13
           ,"n" :14
           ,"o" :15
           ,"p" :16
           ,"q" :17
           ,"r" :18
           ,"s" :19
           ,"t" :20
           ,"u" :21
           ,"v" :22
           ,"w" :23
           ,"x" :24 
           ,"y" :25
           ,"z" :26
             }