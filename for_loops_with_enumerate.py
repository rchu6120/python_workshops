########### enumerate() function: adds a counter to an iterable OBJECT ##########

##### CANNOT CHANGE VALUE OF ORIGINAL DICITONARY 
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    number += 5

print(numbers)

##### iterating WITH enumerate
numbers = [1, 2, 3, 4, 5]

for i, number in enumerate(numbers):
    numbers[i] += 5

print(numbers)

##### iterating WITHOUT enumerate
numbers = [1, 2, 3, 4, 5]
i = 0

for number in numbers:
    numbers[i] += 5
    i += 1

print(numbers)




########### doing the same thing as above without enumerate ##########
numbers = [1, 2, 3, 4, 5]



print(numbers)

numbers[0] += 5
numbers[1] += 5
numbers[2] += 5
numbers[3] += 5
numbers[4] += 5






# what if there were 500 numbers, 1 million?
numbers= list(range(0,500))

for i, number in enumerate(numbers):
    numbers[i] += 5

print(numbers)