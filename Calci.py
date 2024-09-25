print("SIMPLE CALCULATOR".center(35,"*"))
print("Enter the numbers: ")
a=int(input())
b=int(input())
print("Choose the operand:")
print("+  -  *  /  ")
op=input()
if op=="+":
    print("The sum is "+ str(a+b))
elif op=="-":
    print("The difference is " +str( a-b))
elif op=="*":
    print("The product is " + str(a*b))
elif op=="/":
    if b!=0:
        print("The quotient is " + str(a/b))
    else:
        print("Divide by zero error")                
else:
    print("Invalid operand")        