# name = input("Enter your name: ")
# lenght = len(name)
# print("Hello, " + name)
# print("Your name has " + str(lenght) + " letters")


#  lenght = len(input("Enter your name: "))

#  n = "David"
#  l = 5


# print("Výtej v aplikaci vtipných jmen")
# name = input("Jaké je tvé jméno? \n")
# vlastnost = input("Jaká je tvá typická vlastnost? Napiš ji s velkým písmenem \n")
# print("Tvoje vtipné jméno je " + name + " " + vlastnost)


######### Zaokrouhlení round* ########

# print(8/3)
# print(int(8/3))
# print(8 // 3)
# print(round(8/3, 2))


######### operátory ########

# x = 1 
# x = x + 1
# x += 1 
# x *= 2
# x /= 2


######### F string ########

# x = 5 
# print(f"Proměnná x má hodnotu: {x}")
# name = "Dvid"
# age = 35 
# print(f"Jmenuje se {name} a je mu {age} let.")


######### úkol kolid zbýva do konce života ########

# age = int(input("Kolik vám je let: "))
# remain = 90 - age
# months = 12 * remain
# weeks = 52 * remain 
# days = 365 * remain
# print(f"Do konce života vám zbýva {days} dnů, {weeks} týdnů, {months} měsíců respektive {remain} let ") 


######### úkol spropitne ########

# print("Výtejte v kalkulátoru na výpočet plateb. ")
# money = int(input("Kolik máte celkem zaplatit: "))
# spropitne = int(input("Kolik chcete dát spropitného v % "))
# people = int(input("Mezi kolik lidí? "))
# price = (money + (money  * spropitne / 100 )) / people
# final_price = "{:.2f}".format(price)
# print(f"Každý zaplatí {final_price} Kč")


######### Podmínky ########

# print("Výtejte na horské dráze")
# height = int(input("Jaká je vaše výškav cm? \n"))

# if height >= 87:
#     print("Můžete jet na horské dráze.")
# else: 
#     print("Omlouváme se ale nemůžete jet. ")


######### Podmínky - procvičování ########

# age = int(input("Zadejte svůj věk "))

# if age >= 18:
#     print("Jste dospělý ")
# else:
#     print("Nejste dospělý ")


# student = str(input("Jste student? ano/ne "))

# if student == "ano":
#     print("Cena lístku je 120Kč")
# else:
#     print("Cena lístku je 150Kč")


######### Podmínky - normal, smart, extrasmart ########

# type = input("Jaký chcete typ mobilního telefonu? normal smart extrasmart " )

# if type != "normal":
#     print(f"Cena telefonu typu {type} je 25 000Kč")
# else:
#     print(f"Cena telefonu typu {type} je 15 000Kč")


# print("Výtejte na horské dráze")
# height = int(input("Jaká je vaše výškav cm? \n"))

# if height >= 87:
#     print("Můžete jet na horské dráze.")
#     age = int(input("Jaký je váš věk? \n"))
#     if age < 18:
#         print("Cena vaše lístku je 100Kč")
#     else:
#         print("Cena vaše lístku je 150Kč")
# else: 
#     print("Omlouváme se ale nemůžete jet. ")


######### elif ########

# print("Výtejte na horské dráze")
# height = int(input("Jaká je vaše výškav cm? \n"))
# bill = 0

# if height >= 87:
#     print("Můžete jet na horské dráze.")
#     age = int(input("Jaký je váš věk? \n"))
#     if age < 12:
#         bill = 50
#         print("Cena vaše lístku je 50Kč")
#     elif age < 18:
#         bill = 100
#         print("Cena vašeho lístku je 100Kč")
#     else:
#         bill = 150
#         print("Cena vaše lístku je 150Kč")

#     photo = input("Chcete během jízdy vyfotit: ano | ne \n")
#     if photo == "ano":
#         bill = bill + 40
#         # bill += 40
    
#     print(f"Vaše cen je: {bill} Kč")
# else: 
#     print("Omlouváme se ale nemůžete jet. ")


######### Modulo ########

# print(6 % 4) #2 zbytek!
# print(10 % 3) #1
# print(12 % 10) #2


# cislo = int(input("Zadejte číslo \n"))
# if cislo % 2 == 0:
#     print("Sudé číslo")
# else:
#     print("Liché číslo")


######### BMI ########

# height = float(input("Vložte svou výšku v metrech: "))
# weight = float(input("Vložte svou váhu v kg: "))

# bmi = weight / (height * height)

# print(round(bmi, 1))

# if bmi < 18.5:
#     print(f"Vaše bmi je {round(bmi, 1)}, máte podváhu.")
# elif bmi < 24.9:
#     print(f"Vaše bmi je {round(bmi, 1)}, jste v normálu.")
# elif bmi < 29.9:
#     print(f"Vaše bmi je {round(bmi, 1)}, máte nadváhu.")
# elif bmi < 34.9:
#     print(f"Vaše bmi je {round(bmi, 1)}, jste obézní.")
# else:
#     print(f"Vaše bmi je {round(bmi, 1)}, máte extrémní obezitu. Běž běhat!!!")


######### Přestupný rok ########

# year = int(input("Jaký rok chcet zkontrolovat? "))

# if year % 4 == 0:
#     if year % 100 == 0: 
#         if year % 400 == 0: 
#             print("Je to přestupný rok.")
#         else:
#             print("Není to přestupný rok.")
#     else:
#         print("Je to přestupný rok.")
# else:
#     print("Není to přestupný rok.")


######### Úkol Pizza ########

# print("Výtejte v aplikaci na objednání pizzy.")
# size = input("Jakou velikost pizzy chcete? S, M nebo L. ")
# chilli_peppers = input("Chcete feferonky? A nebo N. ")
# extra_cheese = input("Chcete extra sýr? A nebo N. ")

# bill = 0

# if size == "S": 
#     bill += 100
# elif size == "M":
#     bill += 150
# elif size == "L":
#     bill += 200

# if chilli_peppers == "A":
#     if size != "S":
#         bill += 30
#     else:
#         bill += 20

# if extra_cheese == "A":
#     bill += 15
    
# print(f"Částka k zaplacení {bill}Kč. ")


######## Logické operátory ######## and or not

# print("Výtejte na horské dráze")
# height = int(input("Jaká je vaše výškav cm? \n"))
# bill = 0

# if height >= 87:
#     print("Můžete jet na horské dráze.")
#     age = int(input("Jaký je váš věk? \n"))
#     if age < 12:
#         bill = 50
#         print("Cena vaše lístku je 50Kč")
#     elif age >= 12 and age <18:
#         bill += 100
#     elif age < 18:
#         bill = 100
#         print("Cena vašeho lístku je 100Kč")
#     elif age >= 40 and age < 50:
#         bill = 0
#     else:
#         bill = 150
#         print("Cena vaše lístku je 150Kč")

#     photo = input("Chcete během jízdy vyfotit: ano | ne \n")
#     if photo == "ano":
#         bill = bill + 40
#         # bill += 40
    
#     print(f"Vaše cen je: {bill} Kč")
# else: 
#     print("Omlouváme se ale nemůžete jet. ")


######## Harry Potter #######

# print('''
# _                                       _   _            
# | |                                     | | | |          
# | |__   __ _ _ __ _ __ _   _ _ __   ___ | |_| |_ ___ _ __
# | '_ \ / _` | '__| '__| | | | '_ \ / _ \| __| __/ _ \ '__|
# | | | | (_| | |  | |  | |_| | |_) | (_) | |_| ||  __/ |  
# |_| |_|\__,_|_|  |_|   \__, | .__/ \___/ \__|\__\___|_|  
#                         __/ | |                          
#                        |___/|_|                          
# ''')
# print("Vítejte v Bradavicích milí studenti")
# print("Nyní se vypravíte do svých kolejí")


# follow = input("Následovat spolužáky do své nebelvírské koleje? Napište ano nebo ne. ").lower()
# if follow == "ano":
#     stay = input("Jděte po samohýbajících se schodech společně s ostatními. Došli jste do nebelvírské společenské místnosti. Chcete zde zůstat nebo jít po schodech do své ložnice? Napište schody nebo ložnice. ").lower()
#     if stay == "ložnice":
#         print("Krásnou kouzelnou noc.")
#     else:
#         print("Zůstáváte a budete s ostatními ochutnávat kouzelné sladkosti.")
# else:
#     print("Odpojili jste se od svých spolužáků a stojíte sami na chodbě")
#     left_or_right = input("Chcete se vydat doleva nebo doprava? Napište doleva nebo doprava. ").lower()
#     if left_or_right == "doleva":
#         print("Narazili jste na Filche a ten vás vezme do vaší koleje a pošle vás spát")
#     else:
#         door = input("Vidíte před sebou dveře na nádvoří. Chcete jít ven? Napište ven nebo zůstat").lower()
#         if door == "ven":
#             print("Venku je vám zima a raději se vrátíte na svou kolej.")
#         else:
#             print("Stojíš sám na chodbě a nudíš se. Raději se vrátíš do své koleje.")


######### Moduly #########

# import mymodule #můj soubor 

# import random # random 

# print(random.randint(10, 18)) # generování náhodného celého čísla z rozsahu

# print(random.random()) # generování náhodného desetinného čísla mezi 0 až 1

# print(random.randrange(15, 25 , 2)) # generování náhodného celého čísla z rozsahu po dvou 

# import math # matika

# print(math.ceil(5.1)) # ceil (strop) zaokrouhluje nahoru (6)
# print(math.floor(5.1)) # floor (podlaha) zaokrouhluje dolů (5)

# print(math.ceil(random.random() * 6))

# side_coin = random.randint(0,1)
# if side_coin == 0:
#     print("Hlava")
# else:
#     print("Orel")


########## LIST [] ##########

# employees = ["David", "Harry", "Ron"]
# print(employees[0])
# print(employees[1])
# print(employees[2])

# #měnění
# employees[1] = "Hermiona"
# print(employees)

# #přidání
# employees.append("Hermiona")
# print(employees)

# #přidání více položek
# employees.extend(["hermiona", "Kk"])
# print(employees)

# #odstranění
# employees.remove("Ron")
# print(employees)


######### Jak platí bohatí ########

# import random

# names = input("Napiš mi jména všech, ale oddělené čárkou \n")

# list_people = names.split(", ")
# random_number = random.randint(0, len(list_people)-1)

# print(f"{list_people[random_number]} bude dnes platit účet")


# IndexError

# gryffindor = ["david", "Harry", "Ron", "LOL"]
# slytherin = ["Draco", "Crabbe", "Goyle"]

# number = len(gryffindor)
# # print(gryffindor[number])


# # Nested List
#                 #  0           1
# students = [gryffindor, slytherin]
# print(students[0][1])
# print(students[1][2])


########## Lodě #########

# set1 = [ "♥" ,  "♥" ,  "♥" ]
# set2 = [ "♥" ,  "♥" ,  "♥" ]
# set3 = [ "♥" ,  "♥" ,  "♥" ]
# all_sets = [set1, set2, set3]
# print(f"{set1}\n{set2}\n{set3}")
# position = input("Zadejte souřadnice: ")

# num1 = int(position[0])
# num2 = int(position[1])

# all_sets[num1] [num2] = "X"

# print(f"{set1}\n{set2}\n{set3}")


########## Kámen nůžky papír #########

# import random
 
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
 
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
 
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# all_list = [rock, paper, scissors]


# user_choose = int(input("Co si vyberete? Napište 0 pokud kámen, 1 pro papír a 2 pro nůžky\n"))
# user_picture = all_list[user_choose]


# computer_choose = random.randint(0, 2)
# computer_picture = all_list[computer_choose]


# print(f"Uživatel si vybral:\n {user_picture}")
# print(f"Počítač si vybral:\n {computer_picture}")


# if user_choose == computer_choose:
#     print("Remíza")
# elif user_choose == 0 and computer_choose == 1:
#     print("Prohrál jsi, počítač vyhrává")
# elif user_choose == 0 and computer_choose == 2:
#     print("Vyhrál jsi, počítač prohrává")
# elif user_choose == 1 and computer_choose == 0:
#     print("Vyhrál jsi, počítač prohrává")
# elif user_choose == 1 and computer_choose == 2:
#     print("Prohrál jsi, počítač vyhrává")
# elif user_choose == 2 and computer_choose == 0:
#     print("Prohrál jsi, počítač vyhrává")
# elif user_choose == 2 and computer_choose == 1:
#     print("Vyhrál jsi, počítač prohrává")


########## Cyklus FOR #########

# ovoce = ["JABLKO", "HRUŠKA", "POMERANČ"]

# for jedno_ovoce in ovoce:
#     print(jedno_ovoce)


######### Průměrná výška #########

# heights = input("Vložte výšky lidí oddělené čárkou a mezerou\n")
# heights_list = heights.split(", ")
# suma = 0

# for one_height in heights_list:
#     suma = suma + int(one_height)

# average = suma / len(heights_list)
# print(f"Průměrná výška je. {average}.")


######### Nejvyšší skore v testu #########


# score = input("Zadejte skóre jednotlivých studentů oddělené čárkou a mezerou \n ")
# score_list = score.split(", ")
# sln = []
# max = 0

# for index in range(0, len(score_list)):
#    sln.append(int(score_list[index]))

# for one_number in sln:
#    if one_number > max: 
#       max = one_number

# print(f"Maximum je {max}")


########## Range ######### 

# for one_number in range(1, 5):
#     print(one_number)

# Range s kroky 

# for one_number in range(1, 10, 2):
#     print(one_number)

# Suma čísel 

# 1 + 2 + 3 .... + 99 + 100
# 100 + 99 + 98 .... 3 + 2 + 1 
# 100 * 101 / 2 = 5050
# suma = 0

# for one_number in range(1, 101):
#     suma += one_number
# print(suma)

# suma = 0

# for one_number in range(1, 101):
#     if one_number % 2 == 0:
#         suma += one_number

# print(suma)


######### FizzBuzz #########

# for one_number in range(1, 101):
#     if one_number % 3 == 0 and one_number % 5 == 0:
#         print("FizzBuzz")
#     elif one_number % 5 == 0:
#         print("Buzz")
#     elif one_number % 3 == 0:
#         print("Fizz")
#     else:
#         print(one_number)


############ WHILE ############

# x = 0

# while x <= 10:
#     print(f"Já jsem {x} cyklus while")
#     x += 1

# Hádací hra 

# import random

# print("Vítejte v hádací hře Harry Potter")
# characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albus"]
# character = characters[random.randint(0, len(characters) -1)]
# guess = ""
# guess_count = 3
# random_letter = character[random.randint(0, len(character) -1)]


# while character != guess:
#     if guess_count != 0:
#         if guess_count == 1:
#             napoveda = input("Přejete si nápovědu? ano ne\n")
#             if napoveda == "ano":
#                 print(f"Háhodné písmeno slova je {random_letter}")

#         guess = input("Uhodněte postavu z filmu Harry Potter\n")
#         guess_count -=1
#     else:
#         print("Počet pokusů k hádání je vyčerpán")
#         break
#     if character == guess:
#         print(f"Uhádli jste!! Hádané slovo bylo {character}")

# if character != guess:
#     print(f"Neuhodli jste! Hádané slovo bylo {character}")

# Funkce 

# # Přepřipravené funkce 
# print("Ahoj")
# number_character = len("Ahoj")

# # Vlastní funkce 
# def my_function():
#     print("Jmenuji se David")

# my_function()
# my_function()

# def greet():
#     print("Ahoj")
#     print("Na shledanou")

#Funkce s parametrem a argumentem

# def greet_name(name):
#     print(f"Ahoj já jsem {name}")

# greet_name("David")
# name = "David"

# Funkce s více parametry 

# def greet(name, location):
#     print(f"Ahoj já jsem {name} a pocházím z města {location}")

# # positional arguments
# greet("Filip", "Úpice")
# greet("Úpice", "Filip")

# # keyword arguments 
# greet(name="Martina", location="Tábor")
# greet(location="Tábor", name="Martina")

# import math

# height = int(input("Výška zdi: "))
# wight = int(input("Šířka zdi: "))

# meters = height * wight
# cans = 0

# while meters >= 5: 
#     meters -= 5 
#     cans += 1

# print(f"Budete potřebovat {cans} plechovek barvy")

# import math

# height = int(input("Výška zdi: "))
# width = int(input("Šířka zdi: "))
# coverage = 5

# def paint(widht, height, cover):
#     area = widht * height
#     number_can = math.ceil(area / 5) 
#     print(f"Budete potřebovat {number_can} plechovek barvy")

# paint(widht=width, height=height, cover=coverage) 

# Prvočíslo
# def prime_number(number):
#     result = "Je to prvočíslo"
#     for one_number in range(2, number):
#         if number % one_number == 0:
#             result = "Není to prvočíslo"
#     print(result)

# n = int(input("Zadejte prosím číslo: "))

# prime_number(number=n)

# Dictionary
# key - value


# it_dictionary = {
#     "Integer": "Celé číslo",
#     "String": "Text",
#     "Float": "Desetinné číslo",
#     "Boolean": "Pravda nepravda"
# }


# print(it_dictionary["String"])
# print(it_dictionary["Integer"])
# print(it_dictionary["blabla"])


# it_dictionary_2 = {
#     1: "Text",
#     2: "Desetinné číslo",
#     0: "Celé číslo",
#     3: "Pravda nepravda"
# }
# print(it_dictionary_2)
# print(it_dictionary_2[0])
# print(it_dictionary_2[1])
# print(it_dictionary_2[2])

# # Přidání hodnot do dictionary
# it_dictionary_2[4] = "Uložení více hodnot"
# print(it_dictionary_2)

# # Nastavení prázdného dictionary
# empty_dictionary = {}


# # Vyprázdnit dictionary
# it_dictionary_2 = {}


# # Měníme hodnoty v dictionary
# it_dictionary_2[1] = "Textová hodnota"
# print(it_dictionary_2)

# Dictionary a cyklus


# it_dictionary = {
#     "Integer": "Celé číslo",
#     "String": "Text",
#     "Float": "Desetinné číslo",
#     "Boolean": "Pravda nepravda"
# }


# for key in it_dictionary:
#     # print(key)
#     print(it_dictionary[key])

############### Výsledky studentských testů a jejich výsledky ###############

# students_results = {
#   "Harry": 85,
#   "Ron": 71,
#   "Hermione": 98,
#   "Draco": 69
# }

# # Stupnice
# # 91 až 100 = "Excelentní"
# # 81 až 90 = "Vynikající"
# # 71 až 80 = "Splněno"
# # méně jak 71 = "Nesplněno"

# # Tvorba prázdného dictionary
# description_result = {}

# # Převedení bodů na slovní hodnocení
# for key in students_results:
#     score = students_results[key]
#     if score > 90:
#         description_result[key] = "Excelentní"
#     elif score > 80:
#         description_result[key] = "Vynikající"
#     elif score > 70:
#         description_result[key] = "Splněno"
#     else:
#         description_result[key] = "Nesplněno"


# print(description_result)

# Nesting 

cities = {
    "Spain": "Madrid",
    "France": "Paris"
}
# print(cities["Spain"])


# list v dictionary
# travel_diary = {
#     "Spain": ["Madrid", "Leon", "Valencia"],
#     "France": ["Paris", "Nice", "Rennes"]
# }
# print(travel_diary["France"][0])


# dictionary v dictionary
# travel_diary = {
#     "Spain": {"visited_cities": ["Madrid", "Leon", "Valencia"], "visits": 5},
#     "France": {"visited_cities": ["Paris", "Nice", "Rennes"], "visits": 2}
# }
# print(travel_diary["France"]["visited_cities"][1])


# dictionary v listu

# travel_diary = [
#     {
#         "country": "Spain",
#         "visited_cities": ["Madrid", "Leon", "Valencia"],
#         "visits": 5
#     },
#     {
#         "country": "France",
#         "visited_cities": ["Paris", "Nice", "Rennes"],
#         "visits": 2
#     }
# ]
# print(travel_diary[0]["visited_cities"][2])


# travel_diary = [
#     {
#         "country": "Spain",
#         "visited_cities": ["Madrid", "Leon", "Valencia"],
#         "visits": 5
#     },
#     {
#         "country": "France",
#         "visited_cities": ["Paris", "Nice", "Rennes"],
#         "visits": 2
#     },
# ]

# def add_country(country_name, towns_list, visites_number):
#     new_dic = {}
#     new_dic["country"] = country_name
#     new_dic["visited_cities"] = towns_list
#     new_dic["visits"] = visites_number
#     travel_diary.append(new_dic)
    
# add_country("Italy", ["Rome", "Florence", "Milan"], 9)
# print(travel_diary[2]["visits"])
# print(travel_diary[0]["visited_cities"][1])


# funkce a return

# def sum(number1, number2):
#     print(number1 + number2)
# sum(5, 20)

# def better_name(first_name, second_name):
#     first_name = first_name.capitalize()
#     second_name = second_name.capitalize()
#     return f"{first_name} {second_name}"
#     # print(f"{first_name} {second_name}")

# def better_name(first_name, second_name):
#     full_name = first_name + " " + second_name
#     return full_name.title()
    
    
# result = better_name("filip", "HRABA")
# print(result)


############## Funkce a vícekrát return ################

# def better_name(first_name, second_name):
#     if first_name == "" or second_name == "":
#         return "Nevyplnili jste jméno nebo příjmení"
#     full_name = first_name + " " + second_name
#     return full_name.title()

    
# # result = better_name("filip", "")    
# result = better_name(input("Vaše jméno "),input("Vaše příjmení "))
# print(result)

### Return a přestupný rok (procvičování)

# def leap(user_year):
#     if user_year % 4 == 0:
#         if user_year % 100 == 0:
#             if user_year % 400 == 0:
#                 return True
#                 print("Je to přestupný rok")
#             else:
#                 return False
#                 print("Není to přestupný rok")
#         else:
#             return True
#             print("Je to přestupný rok")
#     else:
#         return False
#         print("Není to přestupný rok")

# def days(user_year, user_month):
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     leap_result = leap(user_year)
#     if leap_result == True and user_month == 2:
#         return 29
#     else:
#         return days_in_month[user_month - 1]    
        
# year = int(input("Jaký rok chcete zkontrolovat? "))
# month = int(input("Zadejte měsíc: "))
# result = days(year, month)
# print(f"Počet dnů ve zvoleném měsíci je: {result}")


# Docstring

# def sum(number1, number2):
#     """Vrátí součet dvou čísel"""
#     return number1 + number2

# result = sum(5, 3)
# print(result)


# Local scope a Global scope 

# student1 = "Harry"

# def test():
#     student1 = "David"
#     print(student1)
#     return student1
    
# result = test()
# print(result)


# Block scope 

# number1 = 5 
# # def create_number():
# if number1 < 10: 
#     new_number = 30 
    
# print(new_number)


# Vytvoření globální proměnná
# def test():
#     global my_name
#     my_name = "Harry"
#     print(my_name)


# test()
# print(my_name)


# Konstanty
# PI = 3.14159
# URL = "www.mujweb.cz"


# def calculator():
#     print(PI)


# calculator()


# Debugging (ladění, hladní chyb)


# Popiš problém
# def test_function():     11
#   for number in range(1, 10):
#     if number == 10:
#       print("Vše je správně")
# test_function()


# Občas funguje a občas ne
# import random
# all_dice_numbers = ["1", "2", "3", "4", "5", "6"]
# dice_number = random.randint(1, 6)
                            #  0, 5
# print(all_dice_numbers[dice_number])


# Mysli jako počítač
# year = int(input("Jaký je váš rok narození? "))               
# if year > 1980 and year < 1994:
#   print("Jste millenial.")
         #   =
# elif year > 1994:
#   print("Jste generace Z.")


# Oprav hned chyby
# age = int(input("Kolik je vám let?"))
# if age > 18:
#   print(f"Ve věku {age} můžete kupovat alkohol.")

def change(x_list):
  result_list = []
  for item in x_list:
    item = item + 10
    result_list.append(item)
  print(result_list)


change([1, 2, 3, 4, 5])