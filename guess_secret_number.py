logo = """
            _____                     _                                          
            |  __ \                   (_)                                        
            | |  \/_   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___
            | | __| | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \\
            | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
            \____/\__,_| \___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                                __/ |   __/ |                    
                                               |___/   |___/                      
"""

import random
import os

# Úvodní informace
print(logo)
print("Vítejte ve hře guess secret number. Porazte počítač.")
print("Myslím si číslo od 1 do 100")

# Příprava hry


#Počet pokusů 
def guessing_game():
    attemps = 0
    secret_number = random.randint(1,100)
    difficulty = input("Vyberte si obtížnost. Napište 1 pro 'lehkou' nebo 2 pro 'težkou': ")

    if difficulty == "1":
        attemps = 10
    elif difficulty == "2":
        attemps = 5
    else:
        print("Zadal jste neznámou obtížnost")
        
    another_game = ""
            
    while attemps > 0:
        print(f"Váš počet zbývajících pokusů je {attemps}")
        guess = int(input("Typněte si číslo: "))
        
        if guess < secret_number:
            print("Příliš nízké!")
            attemps -= 1
        elif guess > secret_number:
            print("Příliš vysoké!")
            attemps -= 1
        else:
            print("Vyhráli jste. Počítač poražen!"),
            another_game = input("Napište 'ano', pokud chcete pokračovat. Napište 'ne', pokud chcete hru ukončit ")
            
        if attemps == 0:
            print(f"Prohráli jste hadané číslo bylo {secret_number}. Počítač vyhrál!")
            another_game = input("Napište 'ano', pokud chcete pokračovat. Napište 'ne', pokud chcete hru ukončit ")
            
        if another_game == "ano":
            os.system("cls")
            guessing_game()
        elif another_game == "ne":
            os.system("cls")
            print("Děkujeme že jste hráli.")
            break

guessing_game()