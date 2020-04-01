### 1) Create dictionaries in two different ways to represent the following data:

# Alex purchased a sweater for $300
# Kevin purchased a pair of sneakers for $500
# Henry purchased a pair of sneakers for $500 AND a sweater for $300
# Jason purchased a t-shirt for $200
# Michael purchased a pair of sneakers for $500
# Andrew purchased a t-shirt for $200 AND a sweater for $300

# Organizing the transactions by person
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

# Organizing the transactions by product
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


### 2) Print all of Andrew's purchases along with the price ***
# Code here 

for person, purchase in transactions_by_person.items():
    if person == "Andrew":
        print(transactions_by_person[person])


### 3) Print all of sweater purchases along with the price using ***transactions_by_person***
# Hint: you can use double for loops
# Code here 

for person, purchase in transactions_by_person.items():
    for item, price in purchase.items():
        if item == "sweater":
            print(item, price)


### 4). Insert the string "world" after every "hello" (regardless of upper/lower casing) using a FOR loop
# Hint: you cannot do list.insert(0, "string")

sentence = ["Hello", "my", "name", "is", "Jun.", "I", "like", "to", "say", "hello.", "Every", "time", "I", "write", "code", "in", "a", "new", "language", "I", "print", "hello", "world", "in", "the", "terminal."]


# Code here

for count, word in enumerate(sentence):
    if word == "Hello" or word == "hello" or word == "hello.":
        sentence.insert((count + 1), "world")

print(sentence)

