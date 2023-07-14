import random
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
word_list = ["aardvark", "baboon", "camel"]
tries = 6
chosen_word = word_list[random.randint(0, len(word_list) - 1)] 

wordLength = len(chosen_word)
display = []
for n in range(wordLength):
  display += '_'

print(display)
gameFinished = False

while not gameFinished:
  guess = input('Guess a letter, type here: ').lower()
  hasLetter = False
  print("\n")
  if tries != 0:
    if tries == 1:
      print(f'You have {tries} more try.')
    else:
      print(f'You have {tries} more tries.')
  print(stages[tries])
  if tries == 0:
    gameFinished = True
    print("You have lost this round.")
  
  for n in range(len(chosen_word)):
    if chosen_word[n] == guess:
      display[n] = chosen_word[n]

  if guess not in chosen_word:
      tries -= 1

  if "_" not in display:
    gameFinished = True
    print('You have won this round.')

  print("\n")
  print(*display, sep = ' ')
      
