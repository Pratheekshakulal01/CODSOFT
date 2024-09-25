cont=[]
def phoneDetails():
    nm=input("Enter the name: ")
    phn=input("Enter the phone number: ")
    eml=input("Enter the email: ")
    add=input("Enter the address: ")

    cont.append({
        "name":nm,
        "phone":phn,
        "email":eml,
        "address":add
    })
def viewContact():
    i=1
    print("\n")
    print("CONTACT BOOK")
    for dict in cont:
        print(str(i)+")\n"+"Name: "+dict["name"]+"\n"+"Phone number: "+dict["phone"]+"\n"+"Email: "+dict["email"]+"\n"+"Address: "+dict["address"]+"\n")
        i=i+1
def searchName():
    srch=input("Enter the name or phone number to search: ")
    for dict in cont:
        if srch in dict.values():
            print("Name: "+dict["name"]+"\n"+"Phone number: "+dict["phone"]+"\n"+"Email: "+dict["email"]+"\n"+"Address: "+dict["address"]+"\n")
            return 1
def updateContact():
    idx=int(input("Enter the contact number to be updated: "))-1
    newDict=cont[idx]
    newDict["name"]=input("Enter the new name: ")or newDict["name"]            
    newDict["phone"]=input("Enter the new phone number: ")or newDict["phone"]            
    newDict["emial"]=input("Enter the new email: ")or newDict["email"]            
    newDict["address"]=input("Enter the new address: ")or newDict["address"]            
def deleteContact():
    deln=int(input("Enter the contct number to be deleted: "))-1
    del cont[deln]
      



while(True):
    print("CONTACT BOOK".center(20,"*"))
    print("1.Add contct\n2.View contact list\n3.Search contct\n4.Update contact\n5.Delete contact\n6.Exit ")
    ch=int(input("Enter your choice: "))
    if(ch==1):
       phoneDetails()
    elif(ch==2):
        viewContact()
    elif(ch==3):
       srch=-1
       srch=searchName()
       if(srch==-1):
         print("Doesn't exists")
       
    elif(ch==4):
        updateContact()
    elif(ch==5):
         deleteContact()
    elif(ch==6):
        exit()
    else:
        print("invalid choice")        

