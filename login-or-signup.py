import math

import time

username = raw_input('Enter Username: ')

while len(username) == 0:
    time.sleep(0.5)
    username = raw_input('Username must be greater than zero characters. Please enter a different username: ')

password = raw_input('Enter password: ')

while len(password) <= 7:
    time.sleep(0.5)
    password = raw_input('Password must be at least eight characters. Please enter a different password: ')
    time.sleep(1)

passwordc = raw_input('Confirm password: ')
    
while len(password) != len(passwordc):
    time.sleep(0.5)
    passwordc = raw_input('Please reconfirm password: ')

email = raw_input('Enter your email: ')
    
time.sleep(0.5)

print('Account will be created within 15 hours.')
