#Abdul-Lateef Orulebaja
#program 1

#2.1
for k in range(1,5): #for condition of k
    print(k) #execution if condition is met 

#2.2
halfmid = int(input("What is the height of half pyramid")) #input for half pyramid size
for n in range(1, halfmid+1): #condition for half pyramid range
    print (n*"#",) #execution when condition is met 

#2.3
pmid= int(input("What is the height of the Pyramid")) #
for n in range(1, pmid+1): #range condition for pyramid
    space= pmid-n #distance eqation for spacing 
    t_angle= space * " " + (2*n-1) * "*" #final equation for full "pyramid"
    print(t_angle) #execute pyramid 

#3.1
x=int(input("please enter a number between -15 and 15 ")) #intial variable for part 3
print(x) #checking if function works
eq_1=int((x*x)/4) #equation for porabola 
print(eq_1) #checking if fuction works 

for x in range(-15,16):  #for loop condition to print rotated porabola
    r=eq_1*' '+"#"
    print(r)



   
