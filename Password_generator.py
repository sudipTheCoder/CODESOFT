import random
import string

def generate_password(length):
    """Generates a random password of the specified length."""
    if length < 4:
        return "Password length should be at least 4 characters for better security."
    
    # Define the character pool
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password includes at least one uppercase, one lowercase, one digit, and one special character
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
