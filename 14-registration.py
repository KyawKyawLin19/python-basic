db = {}

def main_sector():
    main_option = int(input("Press 1 to Register:\nPress 2 to Login:\nPress 3 to Exit"))
    if main_option == 1:
        registration()
    elif main_option == 2:
        login()
    elif main_option == 3:
        exit(1)
    else:
        print('Invalid Operation')
        main_sector()

def login():
    print("This is login sector")
    user_found = -1
    login_user_email = input("Enter your email to login:")
    login_user_password = input("Enter your password:")

    for i in range(len(db)):
        if db[i]["email"] == login_user_email and db[i]["password"] == login_user_password:
            user_found = i

        if user_found != i:
            print("Login Success")
            user_profile(login_user_email)
        else:
            print("Username or Password is incorrect")
            
def user_profile(info):
    print('Welcome:', info)

def email_exist(email):
    length = len(db)
    for i in range(length):
        if db[i]["email"] == email:
            return i

def registration():
    email_valid = -1
    user_email = input('Enter your email')
    email_check = email_exist(user_email)
    if email_check != None:
        print('Email already exist')
        registration()
    else:

        user_password = input('Enter your password')

        id = len(db)
        to_insert = {id:{"email" : user_email, "password" : user_password}}
        db.update(to_insert)

if __name__ == '__main__':
    while True:
        main_sector()