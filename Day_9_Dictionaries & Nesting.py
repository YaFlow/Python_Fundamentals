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


                            #Dictionaries and Nesting

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
}


# print(programming_dictionary["Bug"])
#
# programming_dictionary["Loop"]="The action of doing something over and over again",
# print(programming_dictionary)
#
# empty_dictionary={}


#Wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

#Edit an item in a dictionary
# programming_dictionary["Bug"]="A moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])




#Exercitiu

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
#
# for student, score in student_scores.items():
#     if 91 <= score <= 100:
#         student_grades[student] = "Outstanding"
#     elif 81 <= score <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 <= score <= 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)
#

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log-{
#     "France":["Paris","Lille","Dijon"],
#     "Germany":["Stuttgart","Berlin"],
# }



#print Lille
# print(travel_log["France"][1])

nested_list=["A","B",["C","D"]]
# print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visitated": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "Cities_visitated": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },
}
print(travel_log["Germany"]["Cities_visitated"][0])



def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of $ {highest_bid}.")


bids={}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other biddes? Type 'yes' or 'no' . \n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
