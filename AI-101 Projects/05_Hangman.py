import random
import string

# List of words to choose from
word_list = ["python", "developer", "hangman", "programming", "algorithm", "function", "variable", "computer"]

def get_random_word():
    """Random word return karega from word_list"""
    return random.choice(word_list).lower()

def display_hangman(attempts):
    """Har galat guess pe ek part draw hoga"""
    hangman_pics = [
        """
           ------
           |    |
           |    
           |   
           |    
           |    
        """,
        """
           ------
           |    |
           |    O
           |   
           |    
           |    
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |    
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        GAME OVER! 💀
        """
    ]
    return hangman_pics[attempts]

def play_game():
    word = get_random_word()
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()   # User ne jo letters guess kiye hain
    attempts = 0

    print("\n🎩 Welcome to Hangman! Try to guess the word letter by letter.")
    
    while attempts < 6 and len(word_letters) > 0:
        print(display_hangman(attempts))  # Hangman display karega
        print("🔤 Word: " + " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"📢 Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = input("👉 Guess a letter: ").strip().lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("⚠️ Please enter a valid single letter!\n")
            continue

        if guess in guessed_letters:
            print("❌ You already guessed that letter. Try again!\n")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Correct guess!\n")
        else:
            attempts += 1
            print("❌ Wrong guess!\n")

    # Game Over Conditions
    if len(word_letters) == 0:
        print(f"🎉 Congratulations! You guessed the word: {word.upper()}")
    else:
        print(display_hangman(6))
        print(f"💀 Game Over! The word was: {word.upper()}")

def main():
    while True:
        play_game()
        play_again = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
