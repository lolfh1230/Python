# Calculator

import os 

def sum(n1, n2):
    return n1 + n2 

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": sum,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("Jaké je první číslo? "))

    lets_continue = "ano"

    while lets_continue == "ano":
        for symbol in operations:
            print(symbol)
            
        user_symbol = input("Zvolte jednu z operací: ")
        num2 = float(input("Jaké je další číslo? "))


        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)

        print(f"{num1} {user_symbol} {num2} = {result}\n")
        lets_continue = input("Napište ano, pokud chcete pokračovat. Napište po, pro pokračování. Napište ne, pokud chcete kalkulátor spustit znovu ")
        if lets_continue == "ano":
            num1 = result
        elif lets_continue == "po":
            # lets_continue = "ne"
            os.system("cls")
            calculator()
        else:
            print("Kalkulačka ukončena")
            break
            
calculator()