
def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case
    pivot = arr[-1]  # Choose the last element as the pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements smaller than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot
    return quicksort(left) + [pivot] + quicksort(right)

# Example usage
if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Sorted array:", quicksort(arr))
