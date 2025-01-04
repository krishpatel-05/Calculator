print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.division")
print("5.square")
print("6.cube")

choise = int(input("enter your choise=")) 
 
if choise==1:
        a=int(input("enter number:a="))
        b=int(input("enter number:b="))

        print("add of tow number is", int(a+b))

elif choise==2:
        a=int(input("enter number:a="))
        b=int(input("enter number:b="))

        print("sub of tow number is", int(a-b))

elif choise==3:
        a=int(input("enter number:a="))
        b=int(input("enter number:b="))

        print("mul of tow number is", int(a*b))

elif choise==4:
        a=int(input("enter number:a="))
        b=int(input("enter number:b="))

        print("div of tow number is", floata(a/b))

elif choise==5:
        a=int(input("enter number:a="))

        print("square of a number is", int(a**2))
        

elif choise==6:
        a=int(input("enter number:a="))
        
        print("cube of a number is", int(a**3))
        

