#Task-1

def modify_string(txt):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0
    count = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        if count == 3:  # time to consider adding underscore
            count = 0
            # check next char (if exists)
            if i + 1 < len(txt):
                if txt[i + 1] in vowels or txt[i + 1] == "_":
                    # shift underscore one step further (if possible)
                    if i + 2 < len(txt):
                        result += txt[i + 1] + "_"
                        i += 1  # skip the shifted char
                    else:
                        result += txt[i + 1]
                        i += 1
                else:
                    result += "_"
        i += 1

    return result

#Task-2

n = int(input('enter the number:'))

if 1 <= n <= 20:
    for i in range(n):
        print(i**2)
else:
    print('please enter the number between 1 and 20')

#Task-3

i = 1
while i < 11:
    print(i)
    i += 1

#Task-4

rows = 5  # number of lines

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()   #move to the next line

#Task-5

n = int(input('enter the number:'))
total = 0
i = 1
while i <= n:
    total += i
    i=i+1

print(f'the sum of the numbers is {total}')

#Task-6

n = int(input('enter the number:'))
i = 1
while i<= 10:
    print(n*i)
    i=i+1

#Task-7

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0 and num < 500:
        print(num)

#Task-8

numbers = input('enter the number: ')

print('total digits in this number are', len(numbers))

#Task-9

# Number of rows
n = 5

# Outer loop for each row
for i in range(n, 0, -1):
    # Inner loop for printing numbers in reverse order
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()  # Move to the next line

#Task-10

list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i)

#Task-11

i = -10
while i < 0:
    print(i)
    i+=1

#Task-12

i=0
while i<5:
    print(i)
    i+=1

print('Done!')

#Task-13

start = int(input('enter started number: '))
end = int(input('enter ended number: '))
print(f'prime numbers between {start} and {end}:')
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
             print(num)

#Task-14

# Number of terms
n_terms = 10

# First two terms
a, b = 0, 1

print("Fibonacci sequence:")

count = 0
while count < n_terms:
    print(a, end="  ")
    # Update values
    a, b = b, a + b
    count += 1

#Task-15

num = int(input('enter the number:'))
i = 1
factorial = 1
while i <= num:
    factorial = factorial * i
    i = i + 1

print(f'the factorial of the {num} is {factorial}')

#Task-16

def uncommon_elements(list1, list2):
    # Elements in list1 but not in list2
    unique1 = [x for x in list1 if x not in list2]
    
    # Elements in list2 but not in list1
    unique2 = [x for x in list2 if x not in list1]
    
    # Combine both
    return unique1 + unique2
