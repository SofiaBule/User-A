def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Authenticate user (e.g., check credentials against database)
    if check_credentials(username, password):
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None
