def binary_search(arr, target):
    # Performs binary search on a sorted list to find the target value.
    # Returns index of target if found, else -1.
    
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Target not found


# Example
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10
result = binary_search(arr, target)

print("Index:", result)  # Expected output: 4
