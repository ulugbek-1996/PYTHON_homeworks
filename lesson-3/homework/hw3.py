#TASK-1

fruits = ['banana', 'apple', 'peach', 'peer', 'kiwi']

print(fruits[2])

#TASK-2

number1 = [1, 2, 3, 4 ]

number2 = [5, 6, 7, 8 ]

number = number2 + number1

#TASK-3

number = [1, 2, 3, 4, 5, 6, 7]

num1 = number[0]

x = len(number) // 2
num2 = number[x]

num3 = number[-1]

numberall = [num1, num2, num3]

print(numberall)

#TASK-4

movies = ['gentelmen', 'hatiko', 'novda', 'supermen', 'batman']

moviest = tuple(movies)

print(moviest)

#TASK-5 

cities = ['istanbul', 'boku', 'dubay', 'pekin', 'paris']

if 'paris' in cities:

    print('paris is in the list')

else: print('paris is not in the list')

#TASK-6

numbers=[1, 2, 4, 6, 9]

dublicate_numbers = numbers + numbers

print(dublicate_numbers)

#TASK-7

NUMBERS = [1, 3, 5, 7, 9, 11]

NUMBERS[0], NUMBERS[-1] = NUMBERS[-1], NUMBERS[0]

print(NUMBERS)

#TASK-8

TUPLES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

slice_tuple = TUPLES[3:7]

print(slice_tuple)

#TASK-9

COLORS = ['blue', 'green', 'yellow', 'black', 'pillow']

count_blue = COLORS.count('blue')

print(count_blue)

#TASK-10

animals = ('bear', 'lion', 'gepard', 'snake', 'mouse')

index_lion = animals.index('lion')

print(f"lion's index is {index_lion}. ")

#TASK-11

tuple1 = 1, 2, 3, 4

tuple2 = 5, 6, 7, 8

tuple = tuple2 + tuple1

print('merged tuple :', tuple)

#TASK-12

list1 = [1, 3, 5, 7, 9]

tuple1 = (2, 4, 6, 8, 10)

lenl = len(list1)

lent = len(tuple1)

print('len of list: ', lenl)

print('len of tuple: ', lent)

#TASK-13

tuple = 1, 3, 5, 7, 9

list1 = list(tuple)

print(list1)

#TASK-14

tuple = 11, 13, 15, 17, 19, 21

maxtuple = max(tuple)

mintuple = min(tuple)

print(f' maxtuple is {maxtuple} and mintuple is {mintuple} from this tuple')

#TASK-15

my_tuple = 'head', 'arm', 'leg', 'heart', 'stomach'

Revtuple = my_tuple[::-1]

print(f'Reversed tuple is : {Revtuple}')


