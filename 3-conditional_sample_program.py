user_name = 'KKL';
user_pass = 'abc123'
flag = 0
user_input = int(input('Enter some number:'))

# for i in range(user_input):
while True:
    input_name = input('Enter username')
    input_password = input('Enter password')

    if user_name == input_name and user_pass:
        print('login success')
    else:
        flag += 1
        print('login fail')

        if flag >= 3:
            print('Wait a time')
            break
