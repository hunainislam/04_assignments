import random

# Constants
PROMPT: str = "What do you want? (Type 'Joke' to hear a joke or 'Exit' to quit): "
JOKES: list = [
    "Here is a joke for you! Why do programmers prefer dark mode? Because light attracts bugs!",
    "Here is a joke for you! A programmer’s wife tells him: 'Go to the store and buy a loaf of bread. If they have eggs, buy a dozen.' He returns with 13 loaves of bread.",
    "Here is a joke for you! How do you comfort a JavaScript bug? You console it.",
    "Here is a joke for you! Why did the developer go broke? Because he used up all his cache."
]
SORRY: str = "Sorry, I only tell jokes. Try typing 'Joke'."

def main():
    while True:
        user_input = input(PROMPT).strip().lower()
        
        if user_input == "joke":
            print(random.choice(JOKES))  # Selects a random joke from the list
        elif user_input == "exit":
            print("Goodbye! Have a great day. 😊")
            break
        else:
            print(SORRY)

if __name__ == "__main__":
    main()
