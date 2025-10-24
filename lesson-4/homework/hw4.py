#Task-1

# Sample dictionary
my_dict = {
    'apple': 10,
    'banana': 2,
    'cherry': 7,
    'date': 5
}

# Sort dictionary by value (ascending)
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order by value:")
print(ascending)

# Sort dictionary by value (descending)
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("\nDescending order by value:")
print(descending)

#Task-2

my_dict = {0:10, 1:20}

my_dict.update({2:30})

print(my_dict)

#Task-3

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

new_dic = {**dic1, **dic2,**dic3}

print(new_dic)

#Task-4

x = int(input('enter the number: '))

my_dict = {n: n*n for n in range (1, x+1)}

print(my_dict)

#Task-5

my_dict = {n:n*n for n in range(1, 16)}

print(my_dict)

#Task-6

created_set = {1, 2, 3, 4, 5}

print(created_set)

#Task-7

my_set = {'banana', 'apple', 'peach', 'peer', 'orange'}

for item in my_set:

    print(item)

#Task-8

my_set = {'banana', 'apple', 'peach'}

print('my original set :', my_set)

my_set.add('kiwi')

print('after adding 1 item:', my_set)

my_set.update(['pear', 'ananas', 'lemon'])

print('after adding multiple items:', my_set)

#Task-9

my_set = {'banana', 'apple', 'peach', 'kiwi', 'pear', 'ananas', 'lemon'}

print('my original set :', my_set)

my_set.remove('kiwi')

print('after removing 1 item:', my_set)

items_remove = {'banana', 'apple'}

my_set = my_set - items_remove

print('after removing multiple items:', my_set)

#Task-10

my_set = {10, 20, 30, 40, 50}

print("Original set:", my_set)

# Item to remove
item = 60

if item in my_set: 
    my_set.discard(item)
    print(f'{item} was present and removed from set')

else: print(f'{item} is not present in the set')

print('updated set :', my_set)


