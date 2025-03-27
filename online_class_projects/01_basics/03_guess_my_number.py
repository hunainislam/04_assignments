import random

def guess_my_number():
    """Ek interactive number guessing game jo 1 se 99 ke beech secret number guess karne ka moka dega."""
    
    secret_number = random.randint(1, 99)  # Secret number generate karna
    attempts = 0  # User ke attempts track karne ke liye
    max_attempts = 7  # Max guesses allowed

    print("\n🔢 I am thinking of a number between 1 and 99... Can you guess it?")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"({max_attempts - attempts} attempts left) Enter your guess: "))
            
            if guess < 1 or guess > 99:  # Invalid range check
                print("❌ Please enter a number between 1 and 99!")
                continue

            attempts += 1  # Increase attempt count

            if guess < secret_number:
                print("📉 Your guess is too low!\n")
            elif guess > secret_number:
                print("📈 Your guess is too high!\n")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} attempts! The number was: {secret_number}\n")
                break  # Correct guess hone par loop exit
            
        except ValueError:
            print("⚠ Invalid input! Please enter a valid number.\n")

    else:
        print(f"😢 Game Over! The number was: {secret_number}\n")

def main():
    while True:
        guess_my_number()
        replay = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
