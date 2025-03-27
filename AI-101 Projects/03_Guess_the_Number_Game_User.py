import random
import time

def welcome_message():
    print("\n🤖 Welcome to 'Guess the Number' - Computer Edition!")
    print("🧠 Think of a number in your mind, and the computer will try to guess it.")
    print("🔢 You just need to give hints: 'h' (Too High), 'l' (Too Low), 'c' (Correct)\n")

def get_user_feedback():
    while True:
        feedback = input("📢 Enter feedback (h/l/c): ").strip().lower()
        if feedback in ["h", "l", "c"]:
            return feedback
        print("⚠️ Invalid input! Please enter 'h' for too high, 'l' for too low, or 'c' for correct.")

def play_game():
    welcome_message()
    
    while True:
        try:
            lower = int(input("🔢 Enter the lower bound: "))
            upper = int(input("🔢 Enter the upper bound: "))
            if lower >= upper:
                print("❌ Upper bound must be greater than lower bound!")
            else:
                break
        except ValueError:
            print("⚠️ Please enter valid numbers!")

    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        guess = random.randint(lower, upper)
        attempts += 1
        print(f"🤔 Computer guesses: {guess}")
        feedback = get_user_feedback()

        if feedback == "h":
            upper = guess - 1
        elif feedback == "l":
            lower = guess + 1
        elif feedback == "c":
            print(f"🎉 Computer guessed correctly in {attempts} attempts!\n")
            guessed_correctly = True

        if lower > upper:
            print("😕 Seems like there was an issue with the feedback. Please try again.\n")
            break

def main():
    while True:
        play_game()
        play_again = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
