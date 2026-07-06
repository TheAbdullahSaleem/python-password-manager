def add_password():
    website = input("Enter the name of website:    ")
    password = input(f"Enter the password for {website}:     ")
    if website.strip() != "" or password.strip() != "":
        with open("passwords.txt","a") as file:
            file.write(f"{website}:{password}\n")
    else:
        print("You cannot have an empty password or website")
def view_passwords():
    try:
        with open("passwords.txt","r") as file:
            content = file.readlines()
            if len(content) == 0:
                print("Your list is empty")
            else:
                for i in range(len(content)):
                    print(f"{i+1}.{content[i].rstrip()}")
    except FileNotFoundError:
        print("There are currently no tasks")
def search_passwords():
    search = input("Enter the name of website:     ").lower().strip()
    found = False
    try:
        with open("passwords.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                if line.lower().strip().startswith(search):
                    print(line)
                    found = True
            if found == False:
                print("No results found")
    except FileNotFoundError:
        print("Your passwords list is not found or is empty")
def delete_passwords():
    while True:
        while True:
            try:
                try:
                    with open("passwords.txt","r") as file:
                        lines = file.readlines()
                        if len(lines) == 0:
                            print("There are no tasks.")
                            return
                except FileNotFoundError:
                    print("The file is not found or \n there are no passwords")
                    return
                print("Your passwords are")
                view_passwords()
                line_num = int(input("Enter the line number of the password"))-1
            except ValueError:
                print("Please enter a valid choice")
            else:
                break
        if line_num < 0 or line_num >= len(lines):
            print("please choose valid option")
            continue
        else:
            break
    lines.pop(line_num)
    with open("passwords.txt","w") as file:
        for i in range(len(lines)):
            each_line = lines[i]
            file.write(each_line)
    print("Now your tasks are")
    view_passwords()
def option_selection():
    while True:
        while True:
            try:
                user_choice = int(input("""
========== PASSWORD MANAGER ==========

1. Add Passowrd
2. View Passwords
3.Search Password
4. Delete Password
5. Exit:
            """))
            except ValueError:
                print("Please only enter a number not any other thing")
            else:
                break
        if user_choice < 1 or user_choice > 5:
            print("Please enter a valid choice")
            continue
        else:
            break
    return user_choice
def password_book():
    while True:
        user_choice=option_selection()
        if user_choice == 1:
            add_password()
        elif user_choice == 2:
            view_passwords()
        elif user_choice == 3:
            search_passwords()
        elif user_choice == 4:
            delete_passwords()
        elif user_choice == 5:
            print("Goodbye!")
            break
