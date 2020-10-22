num = 10 # state the amount of bottles 
BOTTLES_TO_FALL = 1 # state the constant of how many bottles will fall
while True:
    # check if there are no green bottles
    if num == 0:
        print("there are no green bottles hanging on the wall.")
        input()
        exit(0)
    else:
        print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, and if {BOTTLES_TO_FALL} green bottles should accidentally fall.")
        while True:
            user = int(input("How many green bottles will be hanging on the wall? ")) # take user input to see the next count of bottles to fall
            # check if the user is equal to the num if it is then continue the loop.
            if user == num-BOTTLES_TO_FALL: # check if user is equal to the amount of bottles
                num -= BOTTLES_TO_FALL # if true take away the amount of bottles to fall from the main num
                print(f"There will be {num} green bottles hanging on the wall.") # print success and break the loop
                break
            else:
                print("No, try again.") # user tries again
                continue

