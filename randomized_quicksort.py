
import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case
    pivot_index = random.randint(0, len(arr) - 1)  # Choose a random pivot
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Sorted array:", randomized_quicksort(arr))

