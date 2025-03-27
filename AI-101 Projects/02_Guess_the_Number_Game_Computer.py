import random
import time

def welcome_message():
    print("\n🎯 Welcome to the 'Guess the Number' Game!")
    print("🔢 The computer has selected a random number.")
    print("👀 Your goal is to guess it correctly!\n")

def choose_difficulty():
    print("📌 Choose Difficulty Level:")
    print("1. Easy (1-50, Unlimited Attempts)")
    print("2. Medium (1-100, Max 10 Attempts)")
    print("3. Hard (1-500, Max 7 Attempts)")

    while True:
        try:
            choice = int(input("🎮 Enter your choice (1/2/3): "))
            if choice == 1:
                return 50, None  # Easy Mode: No attempt limit
            elif choice == 2:
                return 100, 10  # Medium Mode: 10 attempts
            elif choice == 3:
                return 500, 7  # Hard Mode: 7 attempts
            else:
                print("❌ Invalid choice! Please select 1, 2, or 3.")
        except ValueError:
            print("⚠️ Enter a valid number (1, 2, or 3).")

def get_user_guess():
    while True:
        try:
            return int(input("🔢 Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")

def play_game():
    welcome_message()
    max_range, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_range)
    
    attempts = 0
    score = 100  # Start with 100 points

    while max_attempts is None or attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("📉 Too Low! Try Again.")
        elif guess > secret_number:
            print("📈 Too High! Try Again.")
        else:
            print(f"🎉 Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            score -= (attempts - 1) * 5  # Reduce score per wrong attempt
            print(f"🏆 Your Score: {max(score, 0)}\n")
            break

    if max_attempts and attempts >= max_attempts:
        print(f"❌ You've used all {max_attempts} attempts! The correct number was {secret_number}.\n")

def main():
    while True:
        play_game()
        play_again = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
