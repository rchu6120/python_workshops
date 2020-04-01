numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print every number greater than 3 within the numbers list
for number in numbers:
    if number > 3:
        print(str(number) + " is greater than 3")

# print every number greater than 3 AND less than 5 within the numbers list
for number in numbers:
    if number > 3 and number < 5:
        print(str(number) + " is greater than 3 but less than 5")


for number in numbers:
    if number > 3 and number < 5:
        # print every number greater than 3 AND less than 5 within the numbers list
        print(str(number) + " is greater than 5 but less than 8")
    elif number > 5 and number < 8:
        # print every number greater than 5 AND less than 8 within the numbers list
        print(str(number) + " is greater than 5 but less than 8")

