#Abdul-Lateef Orulebaja
#LAB 1

#Question A

a=int(input("enter first number"))  #first input
b=int(input("enter second number")) #second imput
print ("the answer is", a/b) #answer statement

#Question B
x_1=int(input('starting x at'))     #input points
y_1=int(input('starting y at'))  #input points
x_2=int(input('ending x at'))  #input points
y_2=int(input('ending y at'))  #input points
print('distance between is', float(((((x_2)-(x_1))^2)+((y_2)-(y_1))^2)))

#Question C
genes=["1.APP","2.GAST","3.INS","4.LCK"] #array values 
for g in genes: #for loop
    print(g) #print list

#Question D
x_f=int(input('factorial of'))
an=1
while (x_f >1):
    an = x_f*an
    x_f= (x_f-1)
print(an)

    



