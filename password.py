import random
import string

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = list(string.digits)
special_chars = list(string.punctuation)

print('Generátor hesel:')
user_letters_count = int(input('Kolik písmen chcete mít ve svém hesle?\n'))
user_digits_count = int(input('Kolik číslic chcete mít ve svém hesle?\n'))
user_specchar_count = int(input('Kolik speciálních znaků chcete mít ve svém hesle?\n'))

user_list_of_characters = random.sample(letters, user_letters_count) + random.sample(numbers, user_digits_count) + random.sample(special_chars, user_specchar_count)
random.shuffle(user_list_of_characters)

mypass = ''
for x in user_list_of_characters:
    mypass += x

print(mypass)