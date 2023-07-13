#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0, len(word_list) - 1)] 
print(chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter, type here: ')
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
hasLetter = False
for n in range(len(chosen_word)):
  if chosen_word[n] == guess:
    hasLetter = True
  print(f'letter {chosen_word[n]}')
print(f'has letter {hasLetter}')    