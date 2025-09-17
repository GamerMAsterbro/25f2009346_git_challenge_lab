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

#main branch
print("Welcome to Library Management!")
pin = int(input("Enter your PIN: "))

if pin == 25477856:  # Superadmin PIN
    superadmin_menu()

elif pin == 7854:  # Employee PIN
    employee_menu()

else:
    print("Invalid PIN. Access denied.")