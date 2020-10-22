names = []

"""
while True:
    selection = int(input("""
#1. Add Name
#2. Delete Name
#3. View Names
#4. Exit
"""))
    if selection == 1:
        names.append(input("Name: "))
    elif selection == 2:
        names.remove(input("Name: "))
    elif selection == 3:
        for i, name in enumerate(names):
            print(i, name)
    elif selection == 4:
        exit(0)

"""

class loop():
    def __init__(self):
        self.names = []
        while True:
            selection = int(input("""
1. Add Name
2. Delete Name
3. View Names
4. Exit
"""))
            if selection == 1:
                self.append_to_list(input("Name: "))
            elif selection == 2:
                self.remove_from_list(input("Name: "))
            elif selection == 3:
                self.list_names()
            elif selection == 4:
                exit(0)
    def append_to_list(self, name):
        self.names.append(name)
    def remove_from_list(self, name):
        self.names.remove(name)
    def list_names(self):
        for i, name in enumerate(self.names):
            print(i, name)
    

loop()