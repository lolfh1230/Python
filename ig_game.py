data = [
    {
        'name': 'Instagram',
        'follower_count': 501,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Facebook',
        'follower_count': 4,
        'description': 'Sociální platforma',
        'country': 'USA'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 436,
        'description': 'Fotbalový hráč',
        'country': 'Portugal'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 161,
        'description': 'Herec a wrestler',
        'country': 'USA'
    },
    {
        'name': 'Harry Potter film',
        'follower_count': 8,
        'description': 'Film',
        'country': 'USA'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 307,
        'description': 'Podnikatelka',
        'country': 'USA'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 324,
        'description': 'Fotbalista',
        'country': 'Argentina'
    },
    {
        'name': 'Neymar',
        'follower_count': 158,
        'description': 'Fotbalista',
        'country': 'Brazilie'
    },
    {
        'name': 'Eminem',
        'follower_count': 40,
        'description': 'Hudebník',
        'country': 'USA'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 193,
        'description': 'Hudebník',
        'country': 'Canada'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 111,
        'description': 'Herečka',
        'country': 'Francie'
    }
]

import random


def account_generator(all_accounts):
    data_length = len(all_accounts)
    random_number = random.randint(0, data_length - 1)
    return all_accounts[random_number]

def printing_options(acc1, acc2):
    print(f"Porovnejte A: {acc1['name']}, {acc1['description']}, {acc1['country']}")
    print(f"Porovnejte B: {acc2['name']}, {acc2['description']}, {acc2['country']}")


def game():
    account_1 = account_generator(data)
    account_2 = account_generator(data)


    right_answer = ""
    score = 0
    lets_continue = True


    while lets_continue:
        # Pro testovací účely
        # print(f"Testovací výpis - účet 1: {account_1['follower_count']}")
        # print(f"Testovací výpis - účet 2: {account_2['follower_count']}")


        printing_options(account_1, account_2)


        user_answer = input("Kdo má více sledujících na instagramu? Napište A nebo B. ")
        if account_1["follower_count"] > account_2["follower_count"]:
            right_answer = "A"
            account_1 = account_2
        else:
            right_answer = "B"
            account_1 = account_2


        if right_answer == user_answer:
            score += 1
            print(f"Uhádli jste. Vaše skóre je {score}")
            account_2 = account_generator(data)
        else:
            print(f"To je špatně. Vaše konečné skóre je {score}")
            lets_continue = False


game()