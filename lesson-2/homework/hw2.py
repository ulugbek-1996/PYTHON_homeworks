# Task-1

from datetime import datetime

name = input('write your name ')

birth_age = int (input('when were you born '))

current_year = datetime.now().year

age = current_year - birth_age

print(f'hello, {name}! you are {age} yaers old.');

# Task-2

txt = 'LMaasleitbtui'
name = "Malibu"

def is_subsequence(text, target):
    it = iter(text)
    return all(char in it for char in target)

if is_subsequence(txt, name):
    print(name)
else:
    print("Name not found");

# Task-3

txt = 'MsaatmiazD'
name = "Matiz"

def is_subsequence(text, target):
    it = iter(text)
    return all(char in it for char in target)

if is_subsequence(txt, name):
    print(name)
else:
    print("Name not found")

# Task-4

txt = "I'am John. I am from London"

# Find the phrase "I am from " and get everything after it
start = txt.find("I am from ")
if start != -1:
    residence = txt[start + len("I am from "):].split()[0]
    print("Residence area:", residence)
else:
    print("Residence area not found.")'''

txt = "I'am John. I am from London"

residence = txt[ len("I'am John. I am from "):]

print("Residence area:", residence);

# Task-5

# Take input from the user
user_input = input("Enter a string: ")

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

# Task-6

# Take input from the user
'''user_input = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize count
count = 0

# Count vowels in the string
for char in user_input:
    if char in vowels:
        count += 1

# Print the number of vowels
print("Number of vowels:", count)

# Task-7

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Maximum value:", max(numbers));

# Task-8

checker = input('enter a word: ')

if checker == checker[::-1]:

 print ('The word is a palindrome.')

else: print('The word is not a palindrome.')

# Task-9

email = input('enter a email: ')

domain = email.split('@')[1]

print('domain:', domain);

# Task-10

import random

# Characters to choose from
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Set password length
length = 12

# Generate password by randomly picking characters
password = ""
for _ in range(length):
    password += random.choice(chars)

print("Random Password:", password);


