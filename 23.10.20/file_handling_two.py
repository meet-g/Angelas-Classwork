text_file = open("users.txt", "r")
end_of_file = False
username = input("Enter your username: ")
while not end_of_file:
    user = text_file.readline().strip()
    if user == "":
        print("User not found")
        end_of_file = True
    if user == username:
        login_date = text_file.readline().strip()
        print("Last logged in on:", login_date)
        end_of_file = True