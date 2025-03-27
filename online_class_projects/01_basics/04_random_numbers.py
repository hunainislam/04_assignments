import random

N_NUMBERS = 10  # Kitne numbers generate karne hain
MIN_VALUE = 1   # Minimum range value
MAX_VALUE = 100 # Maximum range value

def main():
    """10 random numbers generate karega (1-100 ke beech)."""
    
    print("\n🎲 Random Numbers Generated:\n")
    
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Random number print karo

if __name__ == '__main__':
    main()
