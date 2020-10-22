def note_checker(output_value):
    while True:
        selection_two = int(input("""
1. Check Notes
2. Return to main
"""))
        if selection_two == 1:
            note_value = int(input("Note Value (E.G 50, 20, 10, 5): "))
            print(f"{(output_value // note_value)} Note(s) Remainder {output_value % note_value}") 
        elif selection_two == 2:
            break
        else:
            print("Incorrect Input.")

while True:
    selection = int(input("""
1. GBP TO USD
2. GBP TO EUR
"""))
    if selection == 1:
        input_value = float(input('GBP: '))
        print(f"{input_value} Is equal {input_value*1.29} USD")
        note_checker(input_value*1.29)
    elif selection == 2:
        input_value = float(input('GBP: '))
        print(f"{input_value} Is equal {input_value*1.09} EUR")
        note_checker(value*1.09)
    else:
        print("Incorrect Input.")