import random,string
char=string.ascii_letters+string.digits+string.punctuation

def generatePassword(n):
    password=""
    
    for i in range(n):
        password+=random.choice(char)
    print("The password is:     " + password)  


print("WELCOME TO PASSWORD GENERATOR".center(40,"*"))
while(1):
    n=int(input("Enter the password length:\n"))
    if n<6:
        print("The password lenth should be greater than 6!!")
    else:
     generatePassword(n)
     break