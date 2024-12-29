# write a program to translate a message into a secret code language . use the rules below to translate normal english into a secret 
#code language 
#coding :-
# if the word contains atleast 3 character , remove the first letter and append it at the end 
# now append three random characters at the starting and the end 
#else:
#simply reverse the string 

#decoding :
# if the word conatins less than 3 characters reverse it 
#else:
# removes three characters from start and end . now remove the last letter and append it to the beginning 
# your program should ask whether you want to code or decode

#taking string input from user

def encription(str):
    new_string=[]                       #to store the words after encription
    words=str.split(" ")                #splits the string into words 
    for word in words:
        if(len(word)>=3):
            s1="%a&"
            s2="$f@"
            new_word=s1+word[1:] + word[0]+s2       #add 3 random character at the starting and at the end
            new_string.append(new_word)             #appends all the words to the empty list to create a string with encription
        else:
            new_string.append(word[::-1])           # if  the length is less than 3 then just simply reverse it
    print("encrypted message")
    print(" ".join(new_string))                     #convert the list of words into a proper string


def decryption(str):
    new_string=[]
    words=str.split(" ")
    for word in words:
        if(len(word)>=3):
            
            new_word=word[len(word)-4]+word[3:-4]       #remove the first 3 and last 3 random characters and append the last character to first
            
            
            new_string.append(new_word)                 #now add these words to the empty list
        else:
            new_string.append(str[::-1])
    print("decrypted message")
    print(" ".join(new_string))

str=input("enter your message :")
print("press 0 to encrypt your message")
print("press 1 to decrypt your message")

ch=int(input("enter your choice :"))

if(ch==0):
    encription(str)
else:
    decryption(str)
