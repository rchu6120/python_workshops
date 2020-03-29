
user_int = int(input("Please enter an integer. \n"))

while not(type(user_int) == int):
    user_int = int(input("Please enter an integer! \n"))

if user_int % 2 == 0:
    print("Even")
else:
    print("Odd")