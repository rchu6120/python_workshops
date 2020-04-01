x = [1, 2, 3]
y = list(x) # create a NEW list based on the value of x

print(x, y)

if x is y:
    print("equal value and identity") 
elif x == y:
    print("equal value but unqual identity")
else:
    print("unequal")


