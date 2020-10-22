COMPNUM = 50 # state the constant for compnum
count = 1 # state the count.
while  True:
    user_number = int(input("Enter a number: "))
    if user_number == COMPNUM: # Checks if the user input is the same as compnum
        print(f"your guess was correct it has taken you {count} attempts") # Print sucess and tell the user how many tries it took them
        input()
        exit(0)
        # Exit the program after input is pressed.
    else:
        # check if the values are higher / lower than compnum
        if user_number < COMPNUM: # if user_number is less than compnum then say too low
            print("too low")
            count += 1
            continue
        else:
            print("too high") # else print too high
            count +=1

