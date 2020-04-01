########### items() function: return a dictionary's key value pairs ##########

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

for person, purchase in transactions.items():
    print(person, purchase)


# visualizing the iterations

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

counter = 1

for person, purchase in transactions.items():
    print("iteration:", counter, person, purchase)
    counter += 1


# nested iterations

transactions = {
    "alex": 1,
    "kevin": 2,
    "henry": 3
}

for person in transactions.items():
    print(person)

    


