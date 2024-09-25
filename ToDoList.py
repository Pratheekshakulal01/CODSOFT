taskList=[]
print("TO-DO-LST".center(19,"*"))
while(1):
    
    print("\n1.Add task\n2.View task list\n3.Delete task\n4.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        task=input("Enter the task: ")
        taskList.append(task)
        print("The task added successfully: ")
    elif ch==2:
        i=1
        print("\n")
        print("Task list".center(18,"-"))
        for item in taskList:
            print(str(i)+". "+item)
            i=i+1
    elif ch==3:
        if taskList==[]:
            print("The task list is empty")
            print("Nothing to delete")
        else:    
            dn=int(input("Enter the task numberto delete: ") )
            try: 
              del taskList[dn-1]
              print("Task number "+str(dn)+" deleted successfully")
            except IndexError:
                print("No such task exists")
              
    elif ch==4:
        print("THANK YOU")
        exit(0)
    else:
        print("Invalid choice")               
        
