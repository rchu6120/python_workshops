############# Ask the user for an integer
### If it is an even number, print "even"
### If it is an odd number, print "odd"
### If it is not an integer (e.g. character or decimal #), continue asking the user for an input

### THIS PROGRAM SHOULND'T CRASH UNDER THESE CIRCUMSTANCES:
# The user enters an alphabet
# The user enters a decimal number
# The user enters a non numeric character
# The user enters a negative number

# For example, if the user enters "a", the program should ask the user to try again and enter an integer

# Topic: conditionals, user input, loops

# Hint: You can use the try except:


while True:
    try:
        if int(input("Please enter an integer. \n")) % 2 == 0:
            print("even")
            break
        else:
            print("odd")
            break
    except:
        continue