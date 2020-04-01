# Basic while loop 
counter = 1

while counter <= 100:
    print(counter)
    counter += 1


# Condtional while loop 

user_int = int(input("Please enter an integer between 1 and 10"))

# while not(user_int >= 1 and user_int <= 10):
#     user_int = int(input("Please enter an integer between 1 and 10"))

# while user_int <= 1 or user_int >= 10:
#     user_int = int(input("Please enter an integer between 1 and 10"))

print("User entered " + str(user_int))