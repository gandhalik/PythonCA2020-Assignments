# Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and
# if the password is incorrect give chance to enter it again but it should not be more than 3 times.

print('Enter correct username and password combo to continue')
count = 0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password == 'Python12' and username == 'Gandhali':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1
