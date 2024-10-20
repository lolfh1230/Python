import string 
alphabet = list(string.ascii_lowercase + string.ascii_lowercase)

# def encode(message, shift_number):
#     shifted_text = ""
#     for one_letter in message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index + shift_number
#             shifted_text += alphabet[new_index]
#         else:
#             shifted_text += one_letter
#     print(shifted_text)


# def decode(encrypted_msg, shift_number):
#     normal_text = ""
#     for one_letter in encrypted_msg:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index - shift_number
#             normal_text += alphabet[new_index]
#         else:
#             normal_text += one_letter
#     print(normal_text)

def cypher(start_text, shift_number, direction):
    end_text = ""
    for one_letter in start_text:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            if direction == "encode":
                new_index = index + shift_number
                end_text += alphabet[new_index]
            elif direction == "decode":
                new_index = index - shift_number
                end_text += alphabet[new_index]
        else:
            end_text += one_letter
    print(f"Vaše operace byla {direction} a výsledek je {end_text}")

lets = "ano"

while lets == "ano":
    direction = input("Napište 'encode', pokud chcete zakódovat zprávu. Napište 'decode', pokud chcete dekódovat zprávu.\n")
    text = input("Napište svou zprávu: \n").lower()
    shift = int(input("Napište hodnotu posunu:\n"))
    if direction == "encode":
        cypher(text, shift, direction)
        lets = input("Napište ano, pokud chcete pokračocat. Napište ne pokud chcete program ukončit")
    elif direction == "decode":
        cypher(text, shift, direction)
        lets = input("Napište ano, pokud chcete pokračocat. Napište ne pokud chcete program ukončit")