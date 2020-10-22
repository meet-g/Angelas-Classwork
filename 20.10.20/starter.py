def multi(num):
    for i in range(num):
        print(f"{i+1} multiplied by {num} = {num*(i+1)}")

number = int(input("Number: "))
multi(number)
input()