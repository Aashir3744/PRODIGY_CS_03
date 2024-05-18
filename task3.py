import re

def assess_password_strength(password):
    # Define the criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess the strength
    strength_points = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    strength_feedback = []

    if not length_criteria:
        strength_feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        strength_feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        strength_feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        strength_feedback.append("Password should contain at least one number.")
    if not special_criteria:
        strength_feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_level = strength_levels[strength_points]

    return strength_level, strength_feedback

def main():
    while True:
        print("Password Strength Assessment Tool")
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the program.")
            break

        strength_level, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength_level}")

        if feedback:
            print("Feedback:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Your password is very strong!")

        print()  # Blank line for readability

if __name__ == "__main__":
    main()
