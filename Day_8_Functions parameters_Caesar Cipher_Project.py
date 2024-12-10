# This is a sample Python script.
import random
from sys import orig_argv


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


                            #Functions with inputs

# def greet():
#     for salut in range (3):
#         print("Salutare")
# greet()
#Exercitiu

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you today {name}?")
# greet_with_name("Florin")

# Exercitiu

# def life_in_weeks(current_age):
#     weeks=(90*52)-(current_age*52)
#     print(f"You have {weeks} weeks left.")
# life_in_weeks(56)

#Exercitiu
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with("Florin","Romania")

#Exercitiu, greu..

# def calculate_love_score(a, b):
#     name1 = a.lower()
#     name2 = b.lower()
#     first_counter = 0
#     second_counter = 0
#     for same_later in range(0, len(name1)):
#         if name1[same_later] == "t" or name1[same_later] == "r" or name1[same_later] == "u" or name1[
#             same_later] == "e" :
#             first_counter += 1
#
#         if name1[same_later] == "l" or name1[same_later] == "o" or name1[same_later] == "v" or \
#                 name1[same_later] == "e":
#             second_counter += 1
#
#     for same_later in range(0, len(name2)):
#         if name2[same_later] == "t" or name2[same_later] == "r" or name2[same_later] == "u" or name2[
#             same_later] == "e":
#             first_counter += 1
#         if name2[same_later] == "l" or name2[same_later] == "o" or name2[same_later] == "v" or \
#                 name2[same_later] == "e":
#             second_counter += 1
#     print(str(first_counter) + str(second_counter))
# calculate_love_score("Angela Yu", "Jack Bauer")


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type the shift number:\n"))


# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#
#         shifted_position = shifted_position % len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#     return cipher_text


# def decrypt(original_text,shift_amount):
#     cipher_text=""
#     for letter in original_text:
#         unshifted_position=alphabet.index(letter)-shift_amount
#
#         unshifted_position=unshifted_position % len(alphabet)
#         cipher_text+=alphabet[unshifted_position]
#     print(f"Here is the decoded result: {cipher_text}")


def caesar(original_text, shift_amount, encode_or_decode):

    cipher_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
    #return cipher_text

caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

# text_old = encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text_old, shift_amount=shift)
