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

                               #Randomisation and Python LISTS
import random

# random_integer=random.randint(1,10)
# print(random_integer)

# random_number_0_to_1=random.random()
# print(random_number_0_to_1)

# random_float=random.uniform(1,10)
# print(random_float)


#Exercices

# random_integer=random.randint(0,1)
# print(random_integer)
#
# if random_integer==0:
#     print("E cap")
# else:
#     print("E pajura")

                                              #LISTS

# states_of_america=["Delaware","Washington","New-York"]
# states_of_america[1]="Florinton"
# states_of_america.append("Floriland")
# states_of_america.extend(["Iasi","Brasov"])
# print(states_of_america)

#Challenge

friends=["Alice","Boby","Charlie","David","Emanuel"]
random.shuffle(friends)
print(friends[0])
#Sau
print(random.choice(friends))

                                       #Working with Nested Lists


# states_of_america=["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america[49])


# fructe_murdare=["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
#
# print(fructe_murdare)

# fructe=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries"]
# legume=["Spinach","Kale","Tomatoes","Celery","Potatoes"]
#
# fructe_si_legume=[fructe,legume]
#
# print(fructe_si_legume[1][1])#print Kale


#EXERCITIU ROCK PAPER SCISSORS

computer_chooice=["Rock","Paper","Scissors"]
alegere=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(alegere)
# if alegere==0:
print("you picked  " + computer_chooice[alegere])
# elif alegere==1:
#     print("You picked Paper")
# else:
#     print("You picked Scissors")

print("Computer chose:")

# computer_chooice=["Rock","Paper","Scissors"]
random.shuffle(computer_chooice)
print(computer_chooice[0])

if alegere==0 and computer_chooice[0]=="Rock" or alegere==1 and computer_chooice[0]=="Paper" or alegere==2 and computer_chooice[0]=="Scissors":
    print("Egalitate, se reia meciul")
elif alegere==0 and computer_chooice[0]=="Scissors" or alegere==1 and computer_chooice[0]=="Rock" or alegere==2 and computer_chooice[0]=="Paper":
    print("Ai castigat, calculatorul a pierdut")
elif alegere==0 and computer_chooice[0]=="Paper" or alegere==1 and computer_chooice[0]=="Scissors" or alegere==2 and computer_chooice[0]=="Rock":
    print("Ai pierdut, Calculatorul a castigat")
else:
    print("Ai pierdut, calculatorul a castigat")


# O alta rezolvare

# alegere=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
# alegerea_calculatorului=random.randint(0,2)
# print(f"Calculatorul a ales {alegerea_calculatorului}")
#
# if alegere>=3 or alegere<0:
#     print("You typed an invalid number.")
# if alegere==0 and alegerea_calculatorului==2:
#     print("You win!")
# elif alegerea_calculatorului > alegere:
#     print("You lose")
# elif alegerea_calculatorului==alegere:
#     print("Este egalitate")
# elif alegerea_calculatorului==0 and alegere==2:
#     print("You lose")
# elif alegere>alegerea_calculatorului:
#     print("You win!")


