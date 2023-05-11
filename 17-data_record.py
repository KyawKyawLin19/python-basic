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

def recording_all_data():
    with open('data','w') as file:
        for data in db:
            file.write(data)
    file.write('\n')

def loading_all_data():
    print('load')
def login():
    print("This is login sector")
    user_found = -1
    login_user_email = input("Enter your email to login:")
    login_user_password = input("Enter your password:")

    for i in range(len(db)):
        if db[i]["email"] == login_user_email and db[i]["password"] == login_user_password:
            user_found = i

        if user_found != -1:
            print("Login Success!")
            user_profile(user_found)
        else:
            print("Username or Password is incorrect")

def user_profile(user_found):
    print('Welcome:', db[user_found]['u_name'])

    option = int(input('Press 1 to exit'))

    if option == 1:
        recording_all_data()

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
        user_name = input('Enter your name')
        user_password = input('Enter your password')
        user_phone = int(input("Enter your phone:"))
        user_age = int(input("Enter your age:"))

        id = len(db)
        to_insert = {id: {"email": user_email, "u_name" : user_name, "password": user_password, "phone:" : user_phone, "age" : user_age }}
        db.update(to_insert)

if __name__ == '__main__':
    loading_all_data()
    while True:
        main_sector()