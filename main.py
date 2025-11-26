import random
import string
import time
import secrets


def generate_password(length=12):
    """Generates a random secure password."""
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def verify_password(password):
    """Verifies password strength."""
    if len(password) < 12:
        return "Weak: Password must be at least 12 characters.\n Please use special characters."

    """Checks to see if Password has any Uppercase, Lowercase, digits, and/or special characters."""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if not all([has_upper, has_lower, has_digit, has_special]):
        return "Moderate: Password does not meet all criteria. Please use some of these: uppercase, lowercase, numbers, and special characters."

    return "Very Strong: Password meets all of the requirements."

def mfa_otp():
    """Implements MFA with OTP."""
    otp = ''.join(random.choice(string.digits) for i in range(6))
    print(f"Your OTP is: {otp}")
    expiration_time = time.time() + 60  # OTP expires in 60 seconds

    user_otp = input("You have 60 seconds to verify your OTP\nEnter the OTP: ")
    if time.time() > expiration_time:
        print("Your One Time Password expired.")
        return False

    if user_otp == otp:
        print("Multi-Factor Authentication successful!")
        return True
    else:
        print("Wrong One Time Password.")
        return False

def main():
    while True:
        print("\nSelect One of the Following Options:")
        print("Password Generation")
        print("Verify Password Your Strength")
        print("Multi-Factor Authentication Login")

        choice = input("Enter your choice: ")

        if choice == "gen":
            password = generate_password()
            print(f"Generated Password: {password}")

        elif choice == "ver":
            password = input("Please Use Upper and Lowercase characters, as well as Characters such as (@,!,*) \nEnter your password to verify: ")
            print(verify_password(password))

        elif choice == "mfa":
            mfa_otp()

        elif choice == "done":
            break
        else:
            print("Wrong Response. Please Try again.")

if __name__ == "__main__":
    main()