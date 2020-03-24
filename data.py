############ Q1. Change the value of x to 5 and print the sum of x and y ############
# Topic: arithmetic/assignment operators

x = 9
y = 3

# Code here

x = 5
print(x + y)


############ 
# Q2. Change the value of x by the remainder of x divided by 3
# Print the sum of the new value of x and y
############
# Topic: arithmetic/assignment operators

x = 5
y = 2

# Code here

x %= 3
print(x + y)


############ 
# Q3. Print the sum of the 2 results:
# x divided by y  
# y times x
############
# Topic: arithmetic operators
# Hint: Should print 30

x = 9
y = 3

# Code here

print((x / y) + (y * x))


############ Q4.
# 1) Create a new variable, z
# 2) Assign the remainder of x divided by y to variable z
# 3) Multiply the remainder with x 
# 4) Divide x by the result of #3
# 5) Print the value of x (should be 0.5)
# ############
# Topic: arithmetic/assignment operators

x = 8
y = 3

# Code here

z = x % y
i = z * x
x = x / i
print(x)


############# Q5. Print the square root of x IN 2 DIFFERENT WAYS ############
# Topic: arithmetic operators
# Hint: x to what power equals the square root of x?


import math #import the math module
x = 9

# Code here

x = math.sqrt(9)
print(x) 
x = 9**(1/2)
print(x)


############# Q6. print the phrase "hello world" using the 2 variables defined below ############
# Topic: string concatenation

string1 = "hello"
string2 = "world"

# Code here

print(string1 + " " + string2)


############# Q7. Print the phrase "5 dogs" using the 2 variables defined below ############
# Topic: string concatenation

integer = 5
string = "dogs"

# Code here

print(str(integer) + " " + string)


############# Q8. Print the sum of x and string ############
# Topic: string concatenation

x = 3
string = "5"

# Code here

print(x + int(string))

