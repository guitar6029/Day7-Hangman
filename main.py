import random
import wordlist
import hangman
## handman ascii stages art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = wordlist.word_list
tries = 6
chosen_word = word_list[random.randint(0, len(word_list) - 1)] 

wordLength = len(chosen_word)
display = []
for n in range(wordLength):
  display += '_'

print(hangman.hangmanLogo)
print(display)
gameFinished = False
previousGuesses = []

while not gameFinished:
  if len(previousGuesses) > 0 :
    print(f'\n Previous guesses : {previousGuesses}')
  guess = input('Guess a letter, type here: ').lower()
  hasLetter = False
  print("\n")
  if tries != 0:
    if tries == 1:
      print(f'You have {tries} more try.')
    else:
      print(f'You have {tries} more tries.')
  print(stages[tries])
  if "_" not in display:
    gameFinished = True
    previousGuesses = []
    print('You have won this round.')
  
  if tries == 0:
    gameFinished = True
    previousGuesses = []
    print("You have lost this round.")
  
  for n in range(len(chosen_word)):
    if chosen_word[n] == guess:
      display[n] = chosen_word[n]
  previousGuesses.append(guess)

  if guess not in chosen_word:
      tries -= 1

  

  print("\n")
  print(*display, sep = ' ')
      
