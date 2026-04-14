import string
import sys

# LOGIN SIMULATOR

### Past project
def analyze_password(password):
    score = 0
    feedback = []

    ## Common weak passwords
    common_passwords = [
        "password",
        "123456",
        "123456789",
        "qwerty",
        "abc123",
        "password123",
        "admin",
        "letmein"
    ]

    ## Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    ## Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    ## Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    ## Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    ## Special character check
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    ## Common password check
    if password.lower() in common_passwords:
        feedback.append("This password is too common.")
        score = max(score - 2, 0)

    ## Repeated character check
    if len(set(password)) <= 3:
        feedback.append("Avoid too many repeated characters.")
        score = max(score - 1, 0)

    ## Strength result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

### Getting the control information
def initial_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    ## Link to PASSWORD STRENGTH CHECKER (spinoff)
    strength, feedback = analyze_password(password)
    while True:
        if feedback:
            if strength == "Weak" or strength == "Moderate":
                print("\nPassword is " + strength.lower() + ". Please try again.")
            print("Suggestions:")
            for item in feedback:
                print("-", item)
            password = input("Enter your password: ")
            strength, feedback = analyze_password(password)
            continue
        else:
            print("Great password!")
            break
    return username, password

### Main function
def login():
    username, password = initial_login()
    attempts = 0
    failedAttempts_username = []
    failedAttempts_password = []
    "----------------------------------START----------------------------------"
    while attempts < 4:
        userAuthentication_username = input("Please enter the username: ")
        userAuthentication_password = input("Please enter the password: ")
        if userAuthentication_username == username and userAuthentication_password == password:
            print("Login Successful! \nWelcome,", userAuthentication_username)
            break
        elif userAuthentication_username != username:
            attempts += 1
            print("Invalid username or password. \nPlease try again. \nFailed attempts:", attempts)
            failedAttempts_username.append(userAuthentication_username)
            continue
        elif userAuthentication_password != password:
            attempts += 1
            print("Invalid username or password. \nPlease try again. \nFailed attempts:", attempts)
            failedAttempts_password.append(userAuthentication_password)
            continue
    if attempts == 4:
        print("Attempts exceeded. Account is now locked, please try again in 1 hour.")
        return failedAttempts_username, failedAttempts_password
    return True, True


### Code
status_name, status_pass = login()
if status_name is True and status_pass is True:
    sys.exit(0)
else:
    print("Incorrect attempts: ")
if status_name:
    for i in status_name:
        print("- ", i)
if status_pass:
    for j in status_pass:
        print("- ", j)