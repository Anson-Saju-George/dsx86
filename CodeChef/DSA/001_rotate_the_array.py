# Rotate the array

def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is greater than n
    return arr[-k:] + arr[:-k] if k != 0 else arr

# Example usage
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    k = 2
    rotated_array = rotate_array(array, k)
    print("Original array:", array)
    print("Rotated array:", rotated_array)
# Output:
# Original array: [1, 2, 3, 4, 5]
# Rotated array: [4, 5, 1, 2, 3]