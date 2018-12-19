import math

import time

username = input('Enter Username: ')

while len(username) == 0:
    time.sleep(0.5)
    username = input('Username must be greater than zero characters. Please enter a different username: ')

password = input('Enter password: ')

while len(password) <= 7:
    time.sleep(0.5)
    password = input('Password must be at least eight characters. Please enter a different password: ')
    time.sleep(1)

passwordc = input('Confirm password: ')
    
while len(password) != len(passwordc):
    time.sleep(0.5)
    passwordc = input('Please reconfirm password: ')

email = input('Enter your email: ')
    
time.sleep(0.5)

print('Account will be created within 15 hours.')
