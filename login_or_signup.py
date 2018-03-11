
import math

import time

username = input('Enter username: ')

if len(username) == 0:
    time.sleep(0.5)
    username = input('Username must be greater than zero characters. Please enter a different username: ')

time.sleep(1)

password = input('Enter password: ')

if len(password) <= 8:
    time.sleep(0.5)
    password = input('Password must be at least eight characters. Please enter a different password: ')

time.sleep(1)

passwordc = input('Confirm password: ')

if password != passwordc:
    time.sleep(0.5)
    passwordc = input('Please reconfirm password: ')

email = input('Enter your email: ')

time.sleep(0.5)

print('Account will be created within 24 hours.')
