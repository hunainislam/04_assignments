def binary_search_iterative(arr, target):
    """Perform binary search using an iterative approach."""
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        print(f"Checking middle element: {arr[mid]}")  # For visualization

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half
    
    return -1  # Target not found

def binary_search_recursive(arr, target, low, high):
    """Perform binary search using a recursive approach."""
    if low > high:
        return -1  # Base case: Target not found
    
    mid = (low + high) // 2
    print(f"Checking middle element: {arr[mid]}")  # For visualization

    if arr[mid] == target:
        return mid  # Target found at index mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  # Target is in the right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)  # Target is in the left half

def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    target = int(input("Enter the number you want to search: "))
    
    print("Performing binary search using iterative approach...")
    result_iter = binary_search_iterative(arr, target)
    if result_iter != -1:
        print(f"Target {target} found at index {result_iter} using iterative approach.")
    else:
        print(f"Target {target} not found using iterative approach.")
    
    print("\nPerforming binary search using recursive approach...")
    result_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result_rec != -1:
        print(f"Target {target} found at index {result_rec} using recursive approach.")
    else:
        print(f"Target {target} not found using recursive approach.")

if __name__ == "__main__":
    main()
