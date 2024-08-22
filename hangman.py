#hangman
import random
from hangmanhelper import HANGMANPICS, logo, congrats
print(logo)
# Accesses the file with all the possible words, this is going to be a hard game because it's a lot of words
# if you want to use this code, just change the path of the file file to fit how it's going to work on your computer
content = []
with open('C:/Users/a_nie/Downloads/wordlist.txt', 'r') as word:
    content = word.read().split()

# randomly choose a word from content 
chosenWord = random.choice(content)
print(chosenWord)
#the count to for HANGMANPICS index to print which image
count =0

# Create a string of underscores the size of the chosenWord and typecast it as a list to be modified
underscoredWord = list(len(chosenWord) * '_')
lives = 6

# letters that the user already guessed so they dont lose a life or dont get repeated prompts
userGuesses = []
# prompt user to guess a letter
while lives > 0:
    userGuess = input("Guess a letter: ").lower()

    # This block is all for input validation whether its invalid input or repeated input
    
    while not userGuess.isalpha() or len(userGuess) > 1:
        userGuess = input("Invalid input, Guess a letter: ").lower()
    while userGuess in userGuesses:
        userGuess = input("You already guessed this letter, guess again: ")
    if userGuess not in userGuesses: 
        userGuesses.append(userGuess)



    if userGuess in chosenWord: # if the guess is correct, then this replaces the underscore with the correct letter
        for i in range(len(chosenWord)) :
            if userGuess == chosenWord[i]:
                underscoredWord[i] = userGuess
                print(underscoredWord)
    if '_' not in underscoredWord: # if all underscores are replaced, then you have won the game before your lives ran out
        print(congrats)
        print(underscoredWord)
        break;
    
    if userGuess not in chosenWord: #lose a life if you guessed wrong and you get the visual too 
        print("Wrong letter, you've lost a life.")
        count+=1
        print(HANGMANPICS[count])
        lives-=1
        print(f"+++++++++++++++++++++++++++++ {lives}/6 left ++++++++++++++++++++++++++++")
if lives == 0:
    print("GAME OVER, better luck next time losa")
    print(f"BTW, the word was {chosenWord}")

        
