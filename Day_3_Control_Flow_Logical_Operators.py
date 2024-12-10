# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

                               #Control Flow --- Conditional Operators if/else
                               # Module operator 10%5=2
                               #Nested if statements and elif statements
                                #Logical Operators

##### Exercices
# height=int(input('What is your height in cm?'))
#
# if height>=120:
#     print('You can ride the rollercoaster! :)')
# else:
#     print("Sorry, you can't ride the rollercoaster :(")

# number=10%3
# print(number)

##### Exercices
# check_number=int(input('Type a number to see if is Odd or Even'))
# if check_number%2==0:
#     print('Your number is Even :)')
# else:
#     print("Your number is not even :(")

##### Exemple for ELIF
# height=int(input('What is your height in cm?'))
#
# if height >= 120:
#     print('You can ride the rollercoaster! :)')
#     age = int(input('What is your age??'))
#     if age <= 12:
#         print("Pay $5, please")
#     elif age<=18:
#         print("Pay $7, please")
#     else:
#         print("Pay $12, please ")
#
# else:
#     print("Sorry, you can't ride the rollercoaster :(")


##### Exercices
# weight = 85
# height = 1.85
# bmi = weight / (height ** 2)
#
# if bmi < 18.5:
#     print('underweight')
# elif bmi<25:
#     print('normal weight')
# else:
#     print('overweight')




#Exercices

# height=int(input('What is your height in cm?'))
# bill=0
# if height >= 120:
#     print('You can ride the rollercoaster! :)')
#     age = int(input('What is your age??'))
#     if age <= 12:
#         bill=5
#         print("Pay $5, please")
#     elif age<=18:
#         bill = 7
#         print("Pay $7, please")
#     else:
#         bill = 12
#         print("Pay $12, please ")
#
#     wants_photo= input('Do you want a photo ticket ? Type y for Yes and n for No')
#     if wants_photo == "y":
#        bill=bill+3 # sau bill += 3
#
#     print(f'You final bill is ${bill}')
# else:
#     print("Sorry, you can't ride the rollercoaster :(")


# Challenge  Python Pizza ----

# print("Welcome to Python Pizzza Deliveries!! ")
# size=input("What size pizza do you want ? S,M,L or XL : ")
# pepperoni=input("Do you want pepperoni on your pizza? Y or N : ")
# extra_cheese=input("Do you want extra cheese on your pizza? Y or N : ")
# bill=0
#
# if size == "S":
#     bill = 15
#     if pepperoni == "Y":
#         bill = bill + 2
# elif size == "M":
#     bill = 20
#     if pepperoni == "Y":
#         bill = bill + 3
# elif size == "L":
#     bill = 25
#     if pepperoni == "Y":
#         bill = bill + 4
# elif bill =="XL":
#     if pepperoni == "Y":
#         bill = bill + 5
# else:
#     print("You typed something wrong")
# if extra_cheese == "Y":
#     bill = bill + 1
# print(f'You final bill is ${bill}')


#### Final Project for this day---- Treasure Island


print("""
                                 _..-------++._
                             _.-'/ |      _||  \"--._
                       __.--'`._/_\j_____/_||___\    `----.
                  _.--'_____    |          \     _____    /
                _j    /,---.\   |        =o |   /,---.\   |_
               [__]==// .-. \\==`===========/==// .-. \\=[__]
                 `-._|\ `-' /|___\_________/___|\ `-' /|_.'
                       `---'                     `---'
""")


print("Welcome to the Treasure ISLAND")
print("Your mission is to find the treasure")

wrong_choice=input("Let's start, Choose your path, Left or Right? Type your choice : ")
swim_wait=input("Nice,you escaped from traps, now choose your next step, do you want to Swim or Wait?? : ")
door_pick=input("Nice,you escaped from the big fishy, now pick wisely, which door you want to open?? Red, Yellow or Blue ? : ")
if wrong_choice=="Left":
    print(swim_wait)
    if swim_wait== "Wait":
        print(door_pick)
        if door_pick=="Yellow":
            print("Big Boss you won!")
        elif door_pick=="Red":
            print("Burned by fire, game Over, you lose!")
        elif door_pick=="Blue":
            print("Eaten by beasts, game Over, you lose!")
    else:
        print("Attacked by trout.Game over ! ")
else:
    print("Game over ! ")


