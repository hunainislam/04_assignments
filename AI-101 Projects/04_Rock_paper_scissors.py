import random
import time

def get_user_choice():
    """User se input lene ka function (Validations ke saath)"""
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("✊ Rock, 📜 Paper, or ✂️ Scissors? ").strip().lower()
        if user_choice in choices:
            return user_choice
        print("⚠️ Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Computer ka random choice"""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Winner decide karne ka logic"""
    print(f"🧑 You chose: {user}")
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        return "It's a tie! 😐"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "🎉 You win!"
    else:
        return "💀 Computer wins!"

def play_game():
    """Ek round play karne ka function"""
    user_score = 0
    computer_score = 0

    while True:
        print("\n🎮 New Round! 🎮")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)
        print(f"🏆 Result: {result}")

        # Score update
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"📊 Scoreboard: You - {user_score} | Computer - {computer_score}")

        play_again = input("🔄 Play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
