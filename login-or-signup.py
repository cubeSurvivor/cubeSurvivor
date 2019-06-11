import sys

import math

import time

question = input('Login or Signup? (Case sensitive!)')
if question == 'Login':
    time.sleep(0.5)
    already_username = input('Enter your current username: ')           
    already_password = input('Enter your corresponding password: ')
    print('Logging you in now... ')
    time.sleep(0.5)
    sys.exit()

if question != 'Signup' 'Login':
    time.sleep(0.5)
print('Sorry, system does not understand what you are entering.')
time.sleep(0.5)
print('Please try again later.')
time.sleep(0.5)
sys.exit()

if question == 'Signup':
    time.sleep(0.5)    
username = input('Enter Username: ')
while len(username) == 0:
    time.sleep(0.5)
    print('Username must be greater than zero characters.')
    time.sleep(0.5)
    username = input('Please enter a different username: ')
password = input('Enter password: ')
while len(password) <= 7:
    time.sleep(0.5)
    print('Password must be at least eight characters.')
    time.sleep(0.5)
    password = input('Please enter a different password: ')
    time.sleep(0.5)
passwordc = input('Confirm password: ')
while str(password) != str(passwordc):
    time.sleep(0.5)
    passwordc = input('Please reconfirm password: ')
email = input('Enter your email: ')
time.sleep(0.5)
print('Account will be created within 15 hours.')
time.sleep(0.5)
sys.exit()
