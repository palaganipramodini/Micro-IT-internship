import random
import string

def generate_password(length=12):
    if length < 4:
        print("[!] Password length should be at least 4.")
        return None

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        password = generate_password(length)
        if password:
            print(f"[+] Generated Password: {password}")
    except ValueError:
        print("[!] Please enter a valid number.")

if __name__ == "__main__":
    main()
