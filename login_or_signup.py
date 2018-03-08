import math

import Tkinter

import time

username = raw_input('Enter username: ')

if len(username) == 0:
    time.sleep(0.5)
    username = raw_input('Username must be greater than zero characters. Please enter a different username: ')

time.sleep(1)

password = raw_input('Enter password: ')

time.sleep(1)

passwordc = raw_input('Confirm password: ')

if password != passwordc:
   passwordc = raw_input('Please reconfirm password: ')

email = raw_input('Enter your email: ')

time.sleep(0.5)

print('Account will be created within 24 hours.')
