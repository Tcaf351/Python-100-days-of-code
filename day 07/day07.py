# building hangman
import random
from tkinter import dialog

word_list = ["ardvark", "baboon", "camel"]

# step 1 - Randomly choose a word from the word_ist anad assign it to a variable called chosen_word
random_word = random.randint(0, len(word_list)-1)

chosen_word = str(word_list[random_word]) # sets the random word to a string
print(chosen_word)

# step 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase. 
question = input("Guess a letter: \n")

end_of_game = False

while end_of_game == False:
    guess = question.lower() # makes the guess lowercase


# step 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. 
# for letter in chosen_word:
#     if letter == guess:
#         print("right")
#     else:
#         print("wrong")
        

# step 4 - Print "Display" and you should see the guessed letter in the correct position and every other letter replaced with "_". 
        # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that next. 
# for letter in chosen_word:
#     if letter == guess:
#         print(letter)
#     else:
#         print("_")

    display = []
    for letter in range(len(chosen_word)):
        display += '_'

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win")