#$bdul-lateef orulebaja
#Program 4

#2.0
def math_operation():
    fac1=int(input("enter integer")) #first integer input
    fac2=int(input("enter another integer")) #second integer input  
    print("+","\n-","\n*","\n/") #give operator options 
    user_op=input("enter one of the follow mathematic operator") # operator variable for simple calculator

    if user_op == "+" :  # condition set for use of plus sign
        endsum=fac1+fac2 #condtional fuction for plus sign
        return endsum #return answer to possible function
    
    elif  user_op == "-" : # condition set for use of subtraction sign
        endsum=fac1-fac2  #condtional fuction for subtraction sign
        return endsum  #return answer to possible function
    
    elif user_op == "*" : # condition set for use of multiplication sign
        endsum=fac1*fac2  #condtional fuction for multiplication sign
        return endsum  #print answer to possible function
    
    elif user_op== "/": # condition set for use of division sign
        endsum=fac1/fac2  #condtional fuction for division  sign
        return endsum  #return answer to possible function
    else: #if none are applicable 
        return "Invalid Input"

print(math_operation()) #print function

input("\n press enter to continue")

#PART 2

#2.1 String Operaton
#changing forms of string 
def stringChange():
    
    strg = input("Enter string in all caps") #initial string
    new_strg = strg.lower() #executing string function to make all letters lowercase
    strg_dig = new_strg.isdigit
    return strg_dig

print(stringChange()) #print function

input("\n press enter to continue")

#2.2 "Slicing" String in Python
#using basic slicing method and lenght [len()] function

def stringSlice():
    str1 = "to kill a mockiningbird" #string for part 2.2
    
    n = len(str1) #determine length of string str1
    
    f = str1[3:8] #first slice Function
    a = str1[:8] # slicing secong word in string 
    r = str1[8:] # slicing secong half of string phrase 

    return f, a, r # return slices of strinfg 

print(stringSlice()) #print function

input("\n press enter to continue")

#2.3 Breaking Down a simple expression
def simpBreakdown():
    
    expr="12+27" #original expression string
    p1=int(expr[0:2]) #making the 12 an integer
    p2=int(expr[3:]) #making the 27 integer
    newexpr=p1+p2 #making addition of p1 and p2
    return"12+27=",newexpr #return anwer of newexpr

print(simpBreakdown()) #print function

input("\n press enter to continue")



##2.4
# Handling an invalid expression
#handleing the orther operators
#bail out
def validateoperation():
    
    fac1=int(input("enter integer")) #first integer input
    fac2=int(input("enter another integer")) #second integer input
    print("+","\n-","\n*","\n/") #give operator options 
    user_op=input("enter one of the follow mathematic operator") # operator variable for simple calculator

    if user_op == "+" :  # condition set for use of plus sign
        while (True):
            endsum=fac1+fac2 #condtional fuction for plus sign
            return endsum #print answer to possible function
            stop=input("press shift to stop") #terminating possible
            break #stop possible infinite loop
            
    
    elif  user_op == "-" :  # condition set for use of subtraction sign
        while (True):
            endsum=fac1-fac2  #condtional fuction for subtraction sign
            return endsum  #print answer to possible function
            stop=input("press shift to stop")
            break  #stop possible infinite loop
            if stop==input("press shift to stop"):
                exit(endsum)
    
    elif user_op == "*" :  # condition set for use of multiplication sign
        while (True):
            endsum=fac1*fac2  #condtional fuction for multiplication sign
            return endsum  #print answer to possible function
            stop=input("press shift to stop")
            break  #stop possible infinite loop
            if stop==input("press shift to stop"):
                exit(endsum)
    
    elif user_op== "/": # condition set for use of division sign
        while (True):
            endsum=fac1/fac2  #condtional fuction for division  sign
            return endsum  #print answer to possible function
            break #stop possible infinite loop
            stop=input("press shift to stop") #to stop infinite loop
            if stop==input("press shift to stop"):
                exit(endsum)
                
    else: #if no
        return "Invalid Input"

print(validateoperation())

input("\n press enter to continue")

#3.1
#complex expression

def complexoperator():

    def math_operation():
        fac1=int(input("enter integer")) 
        fac2=int(input("enter another integer"))  
        print("+","\n-","\n*","\n/") 
        user_op=input("enter one of the follow mathematic operator") 

        if user_op == "+" :  
            endsum=fac1+fac2 
            return endsum 
    
        elif  user_op == "-" : 
            endsum=fac1-fac2  
            return endsum  
    
        elif user_op == "*" : 
            endsum=fac1*fac2  
            return endsum  
    
        elif user_op== "/": 
            endsum=fac1/fac2  
            return endsum  
        else:  
            return "Invalid Input"
    
    #new variable that represent individual simple calculator expression
    
    operate1 = print(math_operation())
    
    operate2 = print(math_operation())
    
    operate3 = print(math_operation())
    
    #give operator options
    
    print("+","\n-","\n*","\n/")
    first_op = input("please enter your first operator") 
    sec_op = input("please enter your second operator")
    
    #set condition for the intial operator used for complex operations
    
    if first_op == "+" :  
        op_it1 = operat1+operate2 
    
    elif  first_op == "-" :  
        op_it1 = operat1-operate2 
    
    elif first_op == "*" :  
        op_it1 = operat1*operate2 
    
    elif first_op == "/" :  
        op_it1 = operat1/operate2 
    
    else: #if none are applicable 
        return "Cannot complete complex operation"
    
    #set condition for the second operator used for complex operations      

    if sec_op == "+" :  
        op_it2 = op_it1+operate3  
        return op_it1 
    
    elif  sec_op == "-" :  
        op_it2 = op_it1-operate3 
        return op_it2 
    
    elif sec_op == "*" :  
        op_it2 = op_it1*operate3 
        return op_it2 
    
    elif sec_op == "/" :  
        op_it2 = op_it1/operate3 
        return op_it2 
    else:
        return "Cannot complete complex operation"

    
print(complexoperater()) #print function 
