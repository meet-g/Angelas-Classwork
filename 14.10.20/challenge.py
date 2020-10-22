import random

def addition():
    rand1 = random.randint(5, 20)
    rand2 = random.randint(5, 20)
    # Generate two random integers
    two_numbers_added = rand1
    two_numbers_added += rand2
    # add
    print("{} added by {}".format(rand1, rand2))
    # tell user the two numbers
    if int(input("What do the two numbers add to? ")) == two_numbers_added:
        # if correct tell user
        print("You are correct.")
    else:
        # if false tell user
        print("The answer was {}".format(two_numbers_added))

def subtraction():
    rand1 = random.randint(25, 50)
    rand2 = random.randint(25, 50)
     # Generate two random integers
    two_numbers_subtracted = rand1
    two_numbers_subtracted -= rand2
    # subtract
    print("{} subtracted by {}".format(ran1, rand2))
    # tell user the two numbers
    if int(input("What do the two numbers subtract to?")) == two_numbers_subtracted:
        # if correct tell user
        print("You are correct.")
    else:
        # if false tell user
        print("The answer was {}".format(two_numbers_subtracted))

while True:
    #selection menu with integer
    selection = int(input("""
    1. Addition
    2. Subtraction
    """))


    if selection == 1:
        addition()
    elif selection == 2:
        subtraction()
    else: # loop back and let the user try again
        print("Please try again.")
    
