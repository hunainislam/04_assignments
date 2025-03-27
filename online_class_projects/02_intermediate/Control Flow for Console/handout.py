import random

NUM_ROUNDS = 5  # Total rounds
MIN_VALUE = 1   # Minimum range
MAX_VALUE = 100 # Maximum range

def high_low_game():
    print("\n🎮 Welcome to the High-Low Game!")
    print("-" * 40)

    score = 0  # Player ka score track karne ke liye

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\n🔷 Round {round_num}")
        
        player_number = random.randint(MIN_VALUE, MAX_VALUE)  # Player ka number
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)  # Computer ka number

        print(f"Your number is {player_number}")

        # 🚀 Valid input lena (higher/lower)
        while True:
            user_guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if user_guess in ["higher", "lower"]:
                break
            print("⚠️ Please enter either 'higher' or 'lower'.")

        # 🔥 Game Logic (sahi jawab check karna)
        if (user_guess == "higher" and player_number > computer_number) or \
           (user_guess == "lower" and player_number < computer_number):
            print(f"✅ You were right! The computer's number was {computer_number}")
            score += 1  # Score update
        else:
            print(f"❌ Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"🏆 Your score is now {score}")

    # 🏁 **Game Over - Performance Evaluation**
    print("\n🎮 Thanks for playing!")
    if score == NUM_ROUNDS:
        print("🌟 Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("👍 Good job, you played really well!")
    else:
        print("😞 Better luck next time!")

if __name__ == '__main__':
    high_low_game()
