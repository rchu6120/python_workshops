### 1) Create dictionaries in two different ways to represent the following data:

# Alex purchased a sweater for $300
# Kevin purchased a pair of sneakers for $500
# Henry purchased a pair of sneakers for $500 AND a sweater for $300
# Jason purchased a t-shirt for $200
# Michael purchased a pair of sneakers for $500
# Andrew purchased a t-shirt for $200 AND a sweater for $300

# Method 1: Organizing the transactions by person
transactions_by_person = {
    "Alex": {
        "sweater": 300
    },
    "Kevin": {
        "sneakers": 500
    },
    "Henry": {
        "sneakers": 500,
        "sweater": 300
    },
    "Jason": {
        "t-shirt": 200
    },
    "Michael": {
        "sneakers": 500
    },
    "Andrew": {
        "t-shirt": 200,
        "sweater": 300
    }
}

# Method 2: Organizing the transactions by product
transactions_by_product = {
    "sweater": {
        "Alex": 300,
        "Henry": 300,
        "Andrew": 300
    },
    "t-shirt": {
        "Jason": 200,
        "Andrew": 200
    },
    "sneakers": {
        "Kevin": 500,
        "Michael": 500,
        "Henry": 500
    }
}

# Method 3: Organizing the transactions by product without repeating the price
transactions_by_product2 = {
    "sweater": {
        300: ["Alex", "Henry", "Andrew"]
    },
    "t-shirt": {
        200: ["Jason", "Andrew"]
    },
    "sneakers": {
        500: ["Kevin", "Michael", "Henry"]
    }
}

print(transactions_by_product2)

# Method 4: Organizing the transactions by purchase and price in separate dictionaries
price = {
    "sweater": 300,
    "t-shirt": 200,
    "sneakers": 500
}

purchases_by_item = {
    "sweater": ["Alex", "Henry", "Andrew"],
    "t-shirt": ["Jason", "Andrew"],
    "sneakers": ["Kevin", "Michael", "Henry"]
}

purchases_by_person = {
    "Alex": {
        "sweater"
    },
    "Henry": {
        "sweater",
        "sneakers"
    },
    "Michael": {
        "sneakers"
    },
    "Andrew": {
        "sweater",
        "t-shirt"
    },
    "Jason": {
        "t-shirt"
    }
}

print(price)
print(purchases_by_item)
print(purchases_by_person)


### 2) Print all of Andrew's purchases along with the price ***
# Code here 

# Solution 1: double for loops 
for product, order in transactions_by_product.items():
    for person, price in order.items():
        if person == "Andrew":
            print("Andrew purchased a " + product + " for $" + str(price))

# Solution 2: using "in"
for product, order in transactions_by_product.items():
    if "Andrew" in order:
        print("Andrew purchased a " + product + " for $" + str(order["Andrew"]))

# Solution 3: Static/inefficient solution
print("Andrew purchased a sweater for $" + str(transactions_by_person["Andrew"]["sweater"]))
print("Andrew purchased a t-shirt for $" + str(transactions_by_person["Andrew"]["t-shirt"]))


### 3) Print all of sweater purchases along with the price using ***transactions_by_person***
# Hint: you can use double for loops
# Code here 

for person, purchase in transactions_by_person.items():
    for item, price in purchase.items():
        if item == "sweater":
            print(person + " purchased a " + item + " for $" + str(price))


### 4). Insert the string "world" after every "hello" (regardless of upper/lower casing) using a FOR loop
# Hint: you cannot do list.insert(0, "string")

sentence = ["Hello", "my", "name", "is", "Jun.", "I", "like", "to", "say", "hello.", "Every", "time", "I", "write", "code", "in", "a", "new", "language", "I", "print", "hello", "world", "in", "the", "terminal."]


# Code here

for i, word in enumerate(sentence):
    if "HELLO" in word.upper():
        sentence.insert(i + 1, "world")

print(sentence)

