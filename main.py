print("Welcome to Library Management!")
pin = int(input("Enter your PIN: "))

if pin == 25477856:  # Superadmin PIN
    superadmin_menu()

elif pin == 7854:  # Employee PIN
    employee_menu()

else:
    print("Invalid PIN. Access denied.")