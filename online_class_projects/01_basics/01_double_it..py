def main():
    while True:
        try:
            # User se number lene ka input
            curr_value = int(input("Enter a number to start doubling: "))
            break  # Agar valid input hai, to loop se bahar nikle
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print("\nDoubling process starts:\n")
    
    while curr_value < 100:
        curr_value *= 2  # Number ko double karna
        print(curr_value)  # Print result

if __name__ == "__main__":
    main()
