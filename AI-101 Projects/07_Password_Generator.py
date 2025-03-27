import random
import string
import pyperclip  # To copy passwords to clipboard

def generate_password(length=12):
    """Generate a strong random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 Welcome to the Advanced Password Generator!")
    
    while True:
        try:
            num_passwords = int(input("🔢 How many passwords do you want to generate? "))
            length = int(input("🔢 Enter password length: "))
            
            if length < 4:
                print("⚠️ Password length should be at least 4 characters for security!")
                continue
            
            print("\n🔑 Generated Passwords:\n" + "-"*30)
            passwords = [generate_password(length) for _ in range(num_passwords)]
            
            for i, pwd in enumerate(passwords, 1):
                print(f"{i}. {pwd}")
            
            # Copy the first password to clipboard
            pyperclip.copy(passwords[0])
            print("\n📋 First password copied to clipboard!")
        
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue
        
        again = input("\n🔄 Do you want to generate more passwords? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("👋 Thanks for using Password Generator! Stay Secure! 🔒")
            break

if __name__ == "__main__":
    main()
