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

# Hangman
import random
# from test2 import stages


# Uvítání a pravidla hry
print("Vítejte ve hře hádání postav z filmu Harry Potter. Vaším úkolem je...")


# Generování náhodného slova
words = ["harry", "ronald", "albus", "hermiona"]
random_word = words[random.randint(0, 3)]


# Generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")


# Životy
lives = 6
print(stages[lives])


# vypsání slova s podtržítky v normální podobě
printedWord = ""
for one_letter in hidden_word:
    printedWord += one_letter
print(printedWord)


while "_" in hidden_word:
    guess = input("Zadejte hádané písmeno\n").lower()
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess


    # kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    if lives == 0:
        print("Prohráli jste")
        break


    # vypsání slova s podtržítky v normální podobě
    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)


    # kontrola vítězství
    if "_" not in hidden_word:
        print("Vyhráli jste!!!")