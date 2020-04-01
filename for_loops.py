# print every number within the numbers list

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)





# print every number + 5 within the numbers list

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number + 5)

# print(numbers)






# print every number + 5 within the numbers list
# HOW IS THIS DIFFERENT FROM THE PREVIOUS EXAMPLE?

numbers = [1, 2, 3, 4, 5]

# number points to a copy of the actual number
i = 0
for number in numbers:
    numbers[i] += 5
    i += 1
    # number += 5
    # print(number)

print(numbers)
