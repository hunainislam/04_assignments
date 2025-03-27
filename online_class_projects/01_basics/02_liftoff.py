import time  # Time delay ke liye

def countdown(n=10):
    """Countdown function jo given number se 1 tak count karega, fir Liftoff print karega."""
    
    for i in range(n, 0, -1):  # n se 1 tak count
        print(i)
        time.sleep(1)  # Ek second ka delay har print ke baad (Realistic Effect)

    print("🚀 Liftoff! The spaceship has launched! 🚀")

def main():
    while True:
        try:
            user_input = input("Enter countdown start number (default is 10, press Enter to skip): ")
            if user_input.strip() == "":
                countdown()  # Default 10 se countdown karega
            else:
                countdown(int(user_input))  # User-defined countdown
            break  # Valid input milne ke baad loop exit kare
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
