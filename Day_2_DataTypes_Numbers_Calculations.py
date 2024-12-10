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

                                #DATA TYPES


print('Hello'[4]) # imi afiseaza o din Hello
print('123'+'123') # imi da 123123-- se concateneaza

print(23+234) # imi da 257, imi face adunarea

# integers - full number like 123 sau 4 sau 56

#Large Integers
print(123_123_123)

#Float= numar cu virgula
print(3.14159)

#Boolean
#True and False

print(True)
print(False)


# print(type(2))
# print(type("Hello"))
# print(type(True))
# print((type(3.12312)))


# cu str am schimbat data type ul variabilei length_of_name si am putut astfel sa fac calculul
# name_of_the_user=input("Enter your name")
# length_of_name=len(name_of_the_user)
# print('Number of letters in your name:' +str(length_of_name))


# MATHEMATICAL OPERATION

print(3*3)

print(6/2)
print(5/3)
print(5//3) # imi afiseaza intregul fara zecimale
print(2**3) # asa scriu la puterea a 3 a

print(3*(3 + 3/3- 3))#==3


height = 1.65
weight = 84
# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/height**2
print(bmi)
print(int(bmi))
print(round(bmi)) #imi rotunjeste la numarul mai mare


# score=0
# score-=1
# print(score)# imi da -1
#
# print('Your score is '+ str(score))


score = 0
height=1.
is_winning=True
print(f"Your score is = {score} and you height is {height}. You are winning {is_winning}")

# Small Project

#Tip Calculator

print("Welcome to the tip calculator!")
bill=float(input("What was he total bill? "))
tip=int(input('What percentage tip would you like to give? 10,12,15'))
people=int(input("How many people to split the bill?"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
tota_bill=bill+tip_as_percent
bill_per_person=tota_bill/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay $ {final_amount}")























