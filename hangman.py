##### Every program starts with variables: 

    # the hangman word to guess
    # what the user has guessed so far
    # max # of attempts

#### Next you'll need a loop to keep asking the user for their guess

    # The game should keep running as long as there are attempts remaining
    # At each iteration of the loop, it should prompt the user to guess a letter
    # If the user guesses it right, the blanks should be replaced by what the user guessed
    # If the user guesses it wrong, it should print what the user has guessed so far along with the remaining guesses

#### Your program should end when:

    # the user has guessed all of the blanks
    # the user runs out of guesses, and it should print game over

#### What you'll need:

# 1) A string containing the original phrase

# 2) A dictionary storing the letters of the hangman phrase
    # It should have this format: position: {letter: status}
        # POSITION of the letter
        # the LETTER itself
        # STATUS of the letter: guessed/not guessed

    # This is what the generated dictionary looks like. Notice how it has a NESTED structure.
    # guessed_word = {
    #     0: {'H': False}, 
    #     1: {'E': False}, 
    #     2: {'L': False}, 
    #     3: {'L': False}, 
    #     4: {'O': False}, 
    # }

# 3) An integer to keep track of the remaining guesses

########### IMPORTANT: YOUR PROGRAM MUST WORK NO MATTER WHAT THE HANGMAN WORD IS ###########

#### code here ####

word_to_guess = "RICKY IS THE GREATEST"
guessed_characters = {}
number_of_attempts = 6

for i, char in enumerate(word_to_guess):
    guessed_characters[i] = {char: False}

while number_of_attempts > 0:

    #Ask the user for an input
    guess = input("Guess a character \n")

    # Iterates through the FIRST level of the dictionary
    for i, char_info in guessed_characters.items():
        # i is the index (position) of the character
        # char_info is the letter and the status of it: {'H': False}
        
        # Iterates through the SECOND level of the dictionary
        for char, status in char_info.items():
            # If user guesses the letter correctly
            if guess.upper() == char:
                guessed_characters[i][char] = True
                print(char, end = " ")
            # If user guesses the letter INCORRECTLY
            elif guess != char:
                print("_")

    # If the user guesses the letter incorrectly 
    number_of_attempts -= 1

    if number_of_attempts == 0:
        # Print final result
        print(guessed_characters)
    else:
        # Print how many guesses they have remaining 
        print(number_of_attempts)
    
    # If there are no more "False" in the dictionary
        # Let the user know that they won the game            
    
