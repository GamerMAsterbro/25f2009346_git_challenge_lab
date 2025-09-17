# display-rec-fxn branch
def Display_records():
    print("\nWhich File Record Do You Want to Display? ")
    print("1: Book Inventory")
    print("2: Issued Records")
    choice = int(input("Enter your choice (1-2): "))
    if choice == 1:
        with open("Books_data.csv","r",newline='',encoding='utf8') as f:
            reader=csv.reader(f)
            print('\n',"Book Name","\t","Book ID","\t","Quantity Available")
            for i in reader:
                print(i[0],"\t","\t",i[1],"\t","\t",i[2])
                
            
    elif choice == 2:
        with open("Library_Data.csv","r",newline='',encoding='utf8') as f:
            reader=csv.reader(f)
            print('\n',"Borrower Name","\t","Book ID","\t","Book Name","\t","Issue Date","\t","Return Date")
            for i in reader:
                    if len(i)<5:
                        i.append(None)
                        print(i[0],"\t","\t",i[1],"\t","\t",i[2],"\t","\t",i[3],"\t","\t",i[4])
                    else:
                        print(i[0],"\t","\t",i[1],"\t","\t",i[2],"\t","\t",i[3],"\t","\t",i[4])
                
    elif choice != 1 and choice !=2:
        print("Invalid Choice")

#superadmin menu branch
def superadmin_menu():
    print("\nWelcome Superadmin")
    while True:
        print("\nWhat would you like to do?")
        print("1: Add books")
        print("2: Delete Books")
        print("3: Issue a Book")
        print("4: Delete an Issue Record")
        print("5: Record Return Date")
        print("6: Display Records")
        print("7: Leave")
        

        sachoice = int(input("Enter your choice (1-7): "))

        if sachoice == 1:
            add_booknqty()
        elif sachoice == 2:
            bookid = input("Please enter Book ID: ")
            delete_book(bookid)
        elif sachoice == 3:
            name=input("Enter Name: ")
            Bookid=input("Enter Book ID: ")
            Bookname=input("Enter Bookname ")
            issuedate=input("Enter Issue Date ")
            x=[name,Bookid,Bookname,issuedate]
            add_issue_book(x)
        elif sachoice == 4:
            bookid = input("Please enter Book ID: ")
            borrowername = input("Please enter Borrower Name: ")
            del_issue_book(bookid,borrowername)
        elif sachoice == 5:
            bookid = input("Please enter Book ID: ")
            returndate = input("Please enter Return Date: ")
            name=input("Please Enter Browwer Name: ")
            return_issued_book(bookid, returndate, name)
        elif sachoice == 6:
            Display_records()
        elif sachoice == 7:
            print("Exiting Superadmin menu.")
            break
        else:
            print("Invalid choice. Please try again.")
            
#<<<<<<< employee-menu
# employee menu branch
def employee_menu():
    print("\nWelcome Employee")
    while True:
        print("\nWhat would you like to do?")
        print("1: Add books")
        print("2: Issue a Book")
        print("3: Record Return Date")
        print("4: Display Records")
        print("5: Leave")

        sachoice = int(input("Enter your choice (1-5): "))

        if sachoice == 1:
            add_booknqty()
        elif sachoice == 2:
            name=input("Enter Name: ")
            Bookid=input("Enter Book ID: ")
            Bookname=input("Enter Bookname ")
            issuedate=input("Enter Issue Date ")
            x=[name,Bookid,Bookname,issuedate]
            add_issue_book(x)
        elif sachoice == 3:
            bID = input("Please enter Book ID: ")
            returndate = input("Please enter Return Date: ")
            name=input("Please Enter Browwer Name: ")
            return_issued_book(bID, returndate, name)
        elif sachoice == 4:
            Display_records()
        elif sachoice == 5:
            print("Exiting Employee menu.")
            break
        else:
            print("Invalid choice. Please try again.")


#>>>>>>> main
#main branch
print("Welcome to Library Management!")
pin = int(input("Enter your PIN: "))

if pin == 25477856:  # Superadmin PIN
    superadmin_menu()

elif pin == 7854:  # Employee PIN
    employee_menu()

else:
    print("Invalid PIN. Access denied.")