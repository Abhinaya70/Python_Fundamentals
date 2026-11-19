actual_username = "admin"
actual_pwd = "12345"
while True:
    user_name = input("Enter username: ")
    pwd = input("Enter password: ")
    if user_name == actual_username and pwd == actual_pwd:
        print("login successful!")
        break
    else:
        print("Inavalid username or password. Try again!")