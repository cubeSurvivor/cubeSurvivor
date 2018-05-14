icon.png

import math

import tkinter

import time

accountyon = input('Do you have a cubeSurvivor account, yes or no: ')

if len(accountyon) == 'Yes':
    
    input('Please enter your username: ')

    time.sleep(1)

    input('Plesae enter your password: ')

    print('Logging you in now. ')

else:

    username = input('Enter username: ')
    
while len(username) == 0:
    time.sleep(0.5)
    username = input('Username must be greater than zero characters. Please enter a different username: ')
    
time.sleep(1)
    
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

