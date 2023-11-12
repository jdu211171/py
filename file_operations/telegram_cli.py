import json
import re
import sys

user = {}

experience = input('Have you used this program before?\n')
while experience not in ['yes', 'no']:
    experience = input('Please answer to this question with "yes" or "no"\n')

if experience == 'yes':
    with open('./telegram_cli.json', 'r') as file:
        data = json.load(file)

    info = {dct["username"]: dct["password"] for dct in data['users']}
    username = input('Enter your username:\n')
    user_found = False
    for user in data['users']:
        if user['username'] == username:
            user_found = True
            password = input('Enter your password:\n')
            while password != user['password']:
                password = input('Sorry, the password you entered is not correct, please try again:\n')
            print('Welcome to the Matrix!')
            break

    if not user_found:
        print('No users found with this username\n')
        sys.exit()

else:
    with open('./telegram_cli.json', 'r') as file:
        data = json.load(file)

    age = input('Enter your age:\n')
    age = int(age)
    if age < 18:
        print("Sorry, you must be at least 18 years old to use this program.")
        sys.exit()

    username = input('Choose username for your account:\n')
    while username in [dct["username"] for dct in data['users']]:
        username = input('There is already someone with this username, please pick another username:\n')

    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{5,}$'
    compiled_pattern = re.compile(password_pattern)

    password = input('Enter a password:\n')
    while not compiled_pattern.match(password):
        password = input('password chooses must contain at least one character, one number, and one upper and lower '
                         'case letter longer than 8 characters\n')

    status = input('Which status do you want to take, user or admin?\n')
    while status not in ['user', 'admin']:
        status = input('Please answer to this question with "user" or "admin"\n')

    user.update({
        "username": username,
        "age": age,
        "password": password,
        "status": status
    })
    try:
        with open('./telegram_cli.json', 'r') as file:
            data = json.load(file)

        data['users'].append(user)

        with open('./telegram_cli.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError as e:
        print('Sorry we could not saved the data you entered')
        print('Error:', e)

    print('Your account has been created, thanks for using our program\n'
          'Here is your info:\n'
          f'username: {username}\n'
          f'age: {age}\n'
          f'password: {password}\n'
          f'status: {status}')
