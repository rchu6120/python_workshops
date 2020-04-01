############# Q1. Create a list of the first 100 perfect squares and print the result ############
# Topic: lists, loops, conditions, assignment operators
# Hint: Use a WHILE LOOP

# Code here

perfect_squares = []
number = 1

while number <= 100:
    perfect_squares.append(number**2)
    number += 1

print(perfect_squares)


############# Q2. For the following list:
# Print the values that are greater than 100
# Add 1000 to any number that equals to 100
# Delete the values that are less than 100
# Print the final list
############

# Topic: lists, loops, conditions, string concatenation
# Hint: You need to use enumerate()

numbers = [113, 138, 16, 112, 192, 60, 44, 100, 136, 123, 22, 142, 139, 100, 184, 129, 121, 39, 110, 24]

# Code here 

for i, number in enumerate(numbers):
    if number > 100:
        print(number)
    elif number == 100:
        numbers[i] += 1000
    else:
        numbers.remove(number)

print(numbers)
    

############# Q3. Replace every 3rd "a" in the list "STRING" with a "0" USING A FOR LOOP and print the result ############
# Topic: lists, loops, conditions, assignment operators
# Hint: You need to use enumerate()
# print(word) should output: ['a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0, 'a', 'a', 0]

string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
word = []

for char in string:
    word.append(char)

# Code here

for i, letter in enumerate(word):
    if (i + 1) % 3 == 0:
        word[i] = 0

print(word)  


############# Q4. Change the price of everything to 50 USING A LOOP and print the result ############
# Topic: lists, loops, conditions, assignment operators
# Hint: you need to use the str() function

transactions = {
    "Alex": {
        "sweater": 100, 
        "wallet": 10
    },
    "Kevin": {
        "bookbag": 50
        },
    "Henry": {
        "scarf": 500
        }
}

# Code here

for person, purchase in transactions.items():
    for item, price in purchase.items():
        transactions[person][item] = 50

print(transactions)

# Another way to solve this problem

for person, purchase in transactions.items():
    for item in purchase:
        transactions[person][item] = 50

print(transactions)


############# Q5. Give every person's third purchase a 10% discount and print the result ############
# Topic: dictionaries, loops, conditions, assignment operators

transactions = {
    "Alex": {
        "sweater": 100, 
        "wallet": 10, 
        "pen": 1,
    },
    "Kevin": {
        "bookbag": 50,
        "laptop": 1000,
        "soda": 2,
    },
    "Henry": {
        "scarf": 500,
        "t-shirt": 50,
        "hoodie": 100,
        "jacket": 500,
    }
}

# Code here

for person, purchase in transactions.items():
    for item, price in enumerate(purchase.keys()):
        if item == 2:
            purchase[price] *= 0.9

print(transactions)
        
# Another way to solve this problem

for person, purchase in transactions.items():
    for i, item in enumerate(purchase):
        if (i + 1) % 3 == 0:
            transactions[person][item] *= 0.9

print(transactions)


############# Q6. Find the SMALLEST number in the list 'numbers' below and print the value ############
# Topic: lists, loops, conditions

import random
numbers = random.sample(range(1, 1000), 999)

# Code here

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)

# Another way to solve this problem

print(min(numbers))


############# Q7. Find the LARGEST number in the list below USING A FOR LOOP and print the value ############
# Topic: lists, loops, conditions

import random
numbers = random.sample(range(-1000, 1000), 999)
print(numbers)

# Code here

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

print(largest)

# Another way to solve this problem

print(max(numbers))

