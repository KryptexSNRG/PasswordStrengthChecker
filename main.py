import string

def analyze_password(password):
    score = 0
    feedback = []

    # Common weak passwords
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

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("This password is too common.")
        score = max(score - 2, 0)

    # Repeated character check
    if len(set(password)) <= 3:
        feedback.append("Avoid too many repeated characters.")
        score = max(score - 1, 0)

    # Strength result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"


    return strength, feedback


# Main program
password = input("Enter a password to test: ")
strength, feedback = analyze_password(password)

print("\nPassword Strength:", strength)

if feedback:
    print("Suggestions:")
    for item in feedback:
        print("-", item)
else:
    print("Great password!")
