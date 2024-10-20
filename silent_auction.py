import os
auction_logo = '''
         ___________
         \         /
          )_______(
          |"""""""|_.-._,.---------.,_.-._
          |       | | |               | | ''-.
          |       |_| |_             _| |_..-'
          |_______| '-' `'---------'` '-'
          )"""""""(
         /_________\\
         `'-------'`
       .-------------.
      /_______________\\
'''

bidders = {}

print(auction_logo)
print("Vítejte v programu na tichou aukci")
lets = "ano"


while lets == "ano":
    name = input("Jaké je vaše jméno?\n")
    bid = int(input("Jaká je vaše nabídka v dolarech?\n"))
    bidders[name] = bid
    lets = input("Jsou další nabízející? Napište 'ano' nebo 'ne'. ")
    if lets == "ne":
        os.system("cls")  

# highest_bid = 0
# winner = ""

# for key in bidders:
#     if bidders[key] > highest_bid:
#         highest_bid = bidders[key]
#         winner = key

# print(f"Vítězem tiché aukce je: {winner} s nabídkou {highest_bid} dolarů.")

def highest_bid(bidders_dictionary):
    highest_bid = 0
    winner = ""
    for key in bidders_dictionary:
        if bidders_dictionary[key] > highest_bid:
            highest_bid = bidders_dictionary[key]
            winner = key
    print(f"Vítězem tiché aukce je: {winner} s nabídkou {highest_bid} dolarů.")
    
highest_bid(bidders)