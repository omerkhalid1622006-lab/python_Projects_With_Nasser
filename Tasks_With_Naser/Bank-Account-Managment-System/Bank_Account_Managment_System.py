users = {
    "omar":{"Password": "123456", "balance": 0}
}
the_current_user = None
def Register():
    user_name = input("Please Enter Your UserName: ").strip()
    Password = input("Please Enter Your Password: ").strip()
    if(user_name == "" ):
        print("UserName can't be empty.")
        return 
    if(Password == ""):
        print("Password can't be empty.")
        return 
    if(user_name in users):
        print("UserName already exists. Please choose a different UserName")
        return 
    if(len(Password) < 6):
        print("Password must be at least 6 characters long")
        return 
    
    users[user_name] = {'Password':Password , 'balance':0}

    print("Registration successful, You can log in ")
    

def Login():
    user_name = input("Please Enter Your User Name: ").strip()
    Password = input("Please Enter Your Password: ").strip()

    if(user_name not in users ):    # *
        print("UserName does not exist, Please register first.")
        return 
    if(users[user_name]['Password'] != Password):
        print("Incorrect Password, Please try again.")
        return 
    
    global the_current_user
    the_current_user = user_name
    
    print(f"Welcome {user_name}")
    print(f"Current balance: {users[user_name]['balance']} EGP")

    Bank_Menu()


def Bank_Menu():
    while True:
        print("Bank Menu".center(10,"="))

        print("1. Cheak Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Change Password")
        print("6. Logout")

        choice = int(input("Please Enter your choice As a number: "))
        if choice == 1:
            Cheak_Balance()
        elif choice == 2:
            Deposit()
        elif choice == 3:
            Withdraw()
        elif choice == 4:
            Transfer()
        elif choice == 5:
            Change_Password()
        elif choice == 6:
            return 
        else:
            print("Invalid choice")

def Cheak_Balance():
    
    print(f"Current Balance: {users[the_current_user]['balance']} EGP")


def Deposit():
    amount = float(input("Please Enter the amount: "))
    if(amount <= 0):
        print("Invalid amount")
    else:
        users[the_current_user]['balance'] += amount
        print(f"Your Balance Becom {users[the_current_user]['balance']} EGP")
    

def Withdraw():
    amount = float(input("Please enter the amount to withdraw"))
    if(amount <= 0 ):
        print("Amount must be greater than zaro")
        return
    if(amount > users[the_current_user]['balance']):
        print("Insufficient balance.")
        return
    
    users[the_current_user]['balance'] -= amount
    print(f"Successful and Your Balance Become: {users[the_current_user]['balance']} EGP")
    

def Transfer():
    the_recipient_username = input("Plaese Enter the recipient's username ")
    amount = float(input("Please enter the amount to transfer"))
    if the_recipient_username not in users:
        print("This user not included")
        return
    if the_recipient_username == the_current_user:
        print("this transfer is not allowed")
        return
    if(amount > users[the_current_user]['balance']):
        print("Insufficient balance.")
        return
    if(amount <= 0 ):
        print("Amount must be greater than zaro")
        return
    
    users[the_current_user]['balance'] -= amount
    users[the_recipient_username]['balance'] += amount
    print(f"User new balance is {users[the_current_user]['balance']} EGP")
    print(f"User recipient new balance is {users[the_recipient_username]['balance']} EGP")
    

def Change_Password():
    the_current_password = input("Please Enter the current password")
    the_new_password = input("Please enter the new password")
    if(the_current_password != users[the_current_user]["Password"]):
        print("Please again password is not correct")
        return
    if(len(the_new_password) > 6):
        print("Please the password must be at least 6 character long")
        return
    
    # the_new_password = users[the_current_user]['Password']
    users[the_current_user]['Password'] = the_new_password
    print(f"Successfuly and new pasword is {the_new_password}")


def main():
    while True:    
        print("Welcome To Python Bank".center(10,"="))
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Please Choice As a number: "))

        if(choice == 1):
            Register()
        elif(choice == 2):
            Login()
        elif(choice == 3):
            print("Thank you for using python Bank.")
            break
        else:
            print("Invalid choice")

main()

