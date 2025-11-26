import secrets
import string
import time
import hmac
import hashlib

def generate_password(length=16, include_symbols=True, exclude_similar=False):
    """Generates a cryptographically secure password with customizable length and symbols."""
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+=-`~[]\{}|;':,./<>?"
    if exclude_similar:
        characters += characters.replace("P", "0")
        characters += characters.replace("a", "y")
        characters += characters.replace("f", "*")
        characters += characters.replace("H", ")")
        characters += characters.replace("l", "I")
        characters += characters.replace("@", ">")
    return ''.join(secrets.choice(characters) for _ in range(length))

def verify_password_strength(password):
    """Verifies password strength using a more robust approach."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    has_common = password in ["password", "1234", "2025"]

    score = 0
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1

    if has_symbol:
        score += 1
    if not has_common:
        score += 1

    if score >= 6:
        return "Very Strong: Your Password meets all Password Requirements."
    elif score >= 3:
        return "Moderate: Your Password met some of the criteria. Please add more variation Such as (@,!,#,$,%,%,^,&,*)."
    else:
        return "Weak: Password does not meet minimum strength requirements.\nPlease use some of these variations (@,!,#,$,%,%,^,&,*)."

def generate_otp(secret, interval=30):
    """Generates a Time-based One-Time Password (TOTP)."""
    current_time = int(time.time()) // interval
    message = current_time.to_bytes(8, byteorder='big')
    hash_value = hmac.new(secret, message, hashlib.sha256).digest()
    offset = hash_value[-1] & 0x0F
    truncated_hash = int.from_bytes(hash_value[offset:offset + 4], byteorder='big') & 0x7FFFFFFF
    otp = str(truncated_hash % 1000000).zfill(6)
    return otp

def mfa_totp():
    """Implements MFA with TOTP."""
    secret = secrets.token_bytes(32)  # Generate a secure secret
    start_time = time.time() # It records the start time
    otp = generate_otp(secret)
    print(f"Your One Time Password is: {otp}")

    user_otp = input("You have 30 seconds to Enter in the One Time Password. \nEnter the OTP: ")
    end_time = time.time() # It records the end time

    if end_time - start_time > 30:
        print("Your One Time Password is expired. \nPlease try again.")
        return False

    if user_otp == generate_otp(secret):
        print("Multi-Factor Authentication successful!")
        return True
    else:
        print("Wrong One Time Password.")
        return False

def main():
    while True:
        print("\nSelect One of the Following Options:")
        print("Password Generation")
        print("Verify Your Passwords Strength")
        print("Multi-Factor Authentication Login")
        print("Exit")

        choice = input("Enter your choice: ")

        if choice == "gen":
            length = int(input("Strong Passwords are typically 16 characters.\nEnter Your Desired Password Length: ") or 16)
            include_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'
            exclude_similar = input("Exclude similar chartacters? (y/n, default n): ").lower() == 'y'
            password = generate_password(length, include_symbols, exclude_similar)
            print(f"Your Generated Password Is: {password}")

        elif choice == "ver":
            password = input("Enter your password to verify it's strength: ")
            print(verify_password_strength(password))

        elif choice == "mfa":
            mfa_totp()

        elif choice == "done":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()