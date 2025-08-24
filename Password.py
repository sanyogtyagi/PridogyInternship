import re

def evaluate_password(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Determine strength
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")

    strength, feedback = evaluate_password(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()import re

def evaluate_password(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Determine strength
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter your password: ")

    strength, feedback = evaluate_password(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
