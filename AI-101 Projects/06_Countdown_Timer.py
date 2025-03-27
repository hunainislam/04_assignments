import time
import os

def countdown_timer(seconds):
    """Countdown timer function"""
    while seconds:
        mins, secs = divmod(seconds, 60)  # Convert seconds to min:sec format
        timer = f"{mins:02}:{secs:02}"  # Format time
        print(f"⏳ Time Left: {timer}", end="\r")  # Print in same line
        time.sleep(1)
        seconds -= 1
    
    print("\n⏰ TIME'S UP! 🚀")
    play_alarm_sound()

def play_alarm_sound():
    """Play an alarm sound when timer ends"""
    try:
        os.system("echo -e '\a'")  # Beep sound (for Linux & Mac)
    except:
        print("🔔 Beep! Beep!")  # Alternative message

def main():
    while True:
        try:
            seconds = int(input("⏳ Enter countdown time in seconds: "))
            countdown_timer(seconds)
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        again = input("\n🔄 Do you want to start another timer? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("👋 Thanks for using Countdown Timer! Goodbye!")
            break

if __name__ == "__main__":
    main()
