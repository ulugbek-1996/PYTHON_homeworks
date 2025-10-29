#Task-1

year = int(input('enter the year: '))

if (year % 4 == 0 and year % 100 != 0)  or (year % 400 == 0):
    print(f' the {year} is leap year')

else:
    print(f' the {year} is not leap year')

#Task-2

n = int(input('enter the positive number: '))

if n < 1 or n > 100:
    print('the number must be between 1 and 100')
else:


    if n % 2 != 0:
        print('weird')
    elif n % 2 == 0 and n in range (2, 6):
        print('Not Weird')
    elif n % 2 == 0 and n in range (6, 21):
        print('weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

#Task-3


#SOLUTION-1
def print_even_numbers(a, b):
    if a > b:
        return  # base case: stop recursion
    if a % 2 == 0:
        print(a)
    print_even_numbers(a + 1, b)  # recursive call



#SOLUTION-2
a = int(input('enter the number a :'))

b = int(input('enter the number b :'))

c = list(range(a + (a % 2), b + 1, 2))

print(c)
