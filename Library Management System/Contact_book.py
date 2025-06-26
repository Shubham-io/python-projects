import os
name = phone_no = email = " "
while True:
    print("\n__________WELCOME TO CONTACT MANAGEMENT SYSTEM___________\n")
    print("1. Create new contact\n2. Edit existing contact\n3. View contact details\n4. Delete existing contact\n5. Exit")
    choice = int(input())
    if choice == 1:
        while True:
            uname = input("Enter a username: ")
            if uname + '.txt' in os.listdir():
                print("Please enter different user name !")
                break
            name = input("Enter your full name: ")

            phone_no = (input("Enter your phone number in 10 digits:"))
            email = input("Enter your email address: ")

            with open(uname+'.txt', 'a') as file:
                file.write(f"{name}\n{phone_no}\n{email} \n")
                isQuit = input("enter q for quit and 1 for try again:  ")

            if isQuit == 'q':
                break

    elif choice == 2:
        uname = input(("Enter the user name that you want to edit\n"))
        try:
            with open(uname + '.txt', 'r') as f:
                name = f.readline()
                mob = f.readline()
                email = f.readline()
                # print(name,mob,email)

                edit_choice = int(
                    input("What do you want to edit:\n1.Name\n2.Number\n3.Email Id\n"))
            with open(uname + '.txt', 'w') as f:
                if edit_choice == 1:
                    old_name = input("Enter the name: ")
                    new_name = input("Enter the new name: ")
                    set_name = name.replace(old_name, new_name)
                    f.write(set_name + mob + email)
                elif edit_choice == 2:
                    old_num = input("Enter old number: ")
                    new_num = input("Enter new number: ")
                    set_num = data.replace(old_num, new_num)
                    f.write(set_num)
                elif edit_choice == 3:
                    old_id = input("Enter old Email Id: ")
                    new_id = input("Enter new Email Id: ")
                    set_id = data.replace(old_id, new_id)
                    f.write(set_id)
                else:
                    print("Invalid input!")
        except:
            print("File not found or invalid file name")

    elif choice == 3:

        try:
            # userList = os.listdir()
            # for file in userList:
            #     if file.endswith('.txt'):
            #         print("Here are the all users:\n",file)

            # taking user name
            uname = input(("Enter the user name for view details: \n"))
            with open(uname + '.txt', 'r') as f:
                data = f.read()
                print(data)
        except:
            print("File not found or invalid file name")

    elif choice == 4:
        try:
            # taking user name
            uname = input(
                ("Enter the user name whose account you want to delete : \n"))
            os.remove(uname + '.txt')
            print(f"Contact {uname} deleted successfully!")
        except:
            print("File not found or invalid file name")

    elif choice == 5:
        exit()
    else:
        print("Invalid input given!")
        exit()
