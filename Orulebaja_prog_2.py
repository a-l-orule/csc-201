#abdul-lateef orulebaja
#Program 2
#PART 1

fac1=int(input("enter integer")) #first integer input
fac2=int(input("enter another integer")) #second integer input
print("+","\n-","\n*","\n/")
user_op=input("enter one of the follow mathematic operator") # operator variable for simple calculator

if user_op == "+" :  # condition set for use of plus sign
    endsum=fac1+fac2 #condtional fuction for plus sign
    print(endsum) #print answer to possible function
    
elif  user_op == "-" : # condition set for use of subtraction sign
    endsum=fac1-fac2  #condtional fuction for subtraction sign
    print(endsum)  #print answer to possible function
    
elif user_op == "*" : # condition set for use of multiplication sign
    endsum=fac1*fac2  #condtional fuction for multiplication sign
    print(endsum)  #print answer to possible function
    
elif user_op== "/": # condition set for use of division sign
    endsum=fac1/fac2  #condtional fuction for division  sign
    print(endsum)  #print answer to possible function
else: #if no
    print("Invalid Input") 

input("\n press enter to continue")

#PART 2

#2.1 String Operaton
#changing forms of string 

strg = input("Enter string in all caps") #initial string 
new_strg = strg.lower() #executing string function to make all letters lowercase
print("the original string is", strg)  #print original string
print("the new string is", new_strg) #print all lowercase string

input("\n press enter to continue")

#2.2 "Slicing" String in Python
#using basic slicing method and lenght [len()] function 

str1 = "to kill a mockiningbird" #string for part 2.2 
n = len(str1) #determine length of string str1
print(str1[n-4], str1[4], str1[6], str1[5]) #printing specific parts of the string 
f = str1[3:8] #first slice Function
a = str1[:8] # slicing secong word in string 
r = str1[8:] # slicing secong half of string phrase 

print(" ", "|", f , "|") #print first slice function and added string
print(" "*3, "|", a ,"|") #print secong slice and added string
print(" "*5, "|" ,r ,"|") #print third slice and added string

input("\n press enter to continue")

#2.3 Breaking Down a simple expression

expr="12+27" #original expression string
p1=int(expr[0:2]) #making the 12 an integer
print(p1) #checking the integer
p2=int(expr[3:]) #making the 27 integer
print(p2) #checking the integer
newexpr=p1+p2 #making addition of p1 and p2
print("12+27=",newexpr) #print anwer of newexpr

input("\n press enter to continue")


#2.4-7
# Handling an invalid expression
#handleing the orther operators
#put your program within while loop
#bail out

fac1=int(input("enter integer")) #first integer input
fac2=int(input("enter another integer")) #second integer input
print("+","\n-","\n*","\n/")
user_op=input("enter one of the follow mathematic operator") # operator variable for simple calculator

if user_op == "+" :  # condition set for use of plus sign
    while (True):
        endsum=fac1+fac2 #condtional fuction for plus sign
        print(endsum) #print answer to possible function
        stop=input("press shift to stop") #terminating possible 
        if stop==input("press shift to stop"):
            exit(endsum)
    
elif  user_op == "-" :  # condition set for use of subtraction sign
    while (True):
        endsum=fac1-fac2  #condtional fuction for subtraction sign
        print(endsum)  #print answer to possible function
        stop=input("press shift to stop")
        if stop==input("press shift to stop"):
            exit(endsum)
    
elif user_op == "*" :  # condition set for use of multiplication sign
    while (True):
        endsum=fac1*fac2  #condtional fuction for multiplication sign
        print(endsum)  #print answer to possible function
        stop=input("press shift to stop")
        if stop==input("press shift to stop"):
            exit(endsum)
    
elif user_op== "/": # condition set for use of division sign
    while (True):
        endsum=fac1/fac2  #condtional fuction for division  sign
        print(endsum)  #print answer to possible function
        stop=input("press shift to stop") #to stop infinite loop
        if stop==input("press shift to stop"):
            exit(endsum)
else: #if no
    print("Invalid Input")

input("\n press enter to continue")

