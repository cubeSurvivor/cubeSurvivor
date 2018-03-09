import math

import tkinter

import time

cube = input('Do you have a cubeSurvivor account? Yes or no: ')
if 'Yes':
    time.sleep(1)

username = input('Enter your username: ')

time.sleep(1)

password = input('Enter your password: ')

print('Logging in now...')

if 'no' :
    time.sleep(1)

username = input('Enter username: ')

while True:
    (username) == 0
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

