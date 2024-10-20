import random

print("Vítejte v hádací hře Harry Potter")
characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albus"]
print(f"Postavi jsou {characters}")
character = characters[random.randint(0, len(characters) -1)]
guess = ""
guess_count = 3
random_letter = character[random.randint(0, len(character) -1)]


while character != guess:
    if guess_count != 0:
        if guess_count == 1:
            napoveda = input("Přejete si nápovědu? ano ne\n")
            if napoveda == "ano":
                print(f"Háhodné písmeno slova je {random_letter}")

        guess = input("Uhodněte postavu z filmu Harry Potter\n")
        guess_count -=1
    else:
        print("Počet pokusů k hádání je vyčerpán")
        break
    if character == guess:
        print(f"Uhádli jste!! Hádané slovo bylo {character}")

if character != guess:
    print(f"Neuhodli jste! Hádané slovo bylo {character}")
