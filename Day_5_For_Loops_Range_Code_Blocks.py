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



                                       #For Loops Range and Code Blocks ! !
#model for a for loop

# fruits=["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

student_scores=[150,142,120,171,184,149,24,59,68,1,59,68,199,86]
total_exam_score=sum(student_scores)

sum=0
for score in student_scores:
    sum+=score
print(sum) # cu for am facut suma tuturor numerelor din paranteza, insa puteam sa facem tot doar cu sum, fara sa mai scriem forul


# max_score=max(student_scores)
# print(max_score)


#exercitiu ca sa scriem for in loc de max, fara sa folosesc functia max

# max_score=0
# for maximum in student_scores:
#     if maximum>max_score:
#         max_score=maximum
# print(max_score)


# Range function

# random_sum=0
# for number in range(1,101): # cu 3 pot sa precizez pasii din cat in cat sa imi faca numaratoarea
#     random_sum+=number
#     print(random_sum)


#Challenge---Solved

# for number in range(1,101):
#
#     if number%3==0 and number %5==0:
#         print("FizzBuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number %5==0:
#         print("Buzz")
#     else:
#         print(number)


# Final project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy lvl

# print(random.choice(letters))
# parola=parola + random.choice(letters)

parola=""
for i in range(0,nr_letters):
    parola = parola + random.choice(letters)
print(parola)

for j in range(0,nr_symbols):
    parola = parola + random.choice(symbols)
print(parola)

for k in range(0,nr_numbers):
    parola = parola + random.choice(numbers)

finaly_password=list(parola)
random.shuffle(finaly_password)
result="".join(finaly_password)
print(result)







