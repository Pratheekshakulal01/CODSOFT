import random
op=["rock","paper","scissor"]
cscore=0
uscore=0
def checkWinner(user,comp):
    global cscore,uscore
    if user.lower()=="rock" and comp=="scissor" or user.lower()=="scissor" and comp=="paper" or user.lower()=="paper" and comp=="rock":
        print("User wins.")
        uscore= uscore+1
        print("User:"+str(uscore)+"                 "+"Computer:"+str(cscore))

    elif user.lower()==comp:
        print("It's a tie.")  
        uscore= uscore+1  
        cscore=cscore+1
        print("User:"+str(uscore)+"                 "+"Computer:"+str(cscore))

    else:
        print("Computer wins.")
        cscore=cscore+1
        print("User:"+str(uscore)+"                 "+"Computer:"+str(cscore))

print("\nRock Paper Scissor [enter 'exit' to exit]")
while(1):
    user=input("\nEnter: ")
    if(user.lower()=="exit"):
        break
    if(user.lower()!="rock" and user.lower()!="paper" and user.lower()!="scissor"):
        print("Inavlid choice")
        continue
    comp=random.choice(op)
    print("\n")
    print("User: "+user+"                 "+"Computer: "+comp)
    # print("User:"+str(uscore)+"                 "+"Computer:"+str(cscore))
    
    checkWinner(user,comp)
print("User score: "+ str(uscore))
print("Computer score: "+str(cscore))
if cscore<uscore:
    print("USER IS THE WINNER!!!")
else:
    print("COMPUTER IS THE WINNER!!!")    
