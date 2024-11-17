import time
import random
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort

# Function to generate different types of input arrays
def generate_array(size, array_type):
    if array_type == "Random":
        return [random.randint(1, size) for _ in range(size)]
    elif array_type == "Sorted":
        return list(range(size))
    elif array_type == "Reverse-Sorted":
        return list(range(size, 0, -1))

# Array sizes and types to test
sizes = [1000, 5000, 10000]  # Array sizes
array_types = ["Random", "Sorted", "Reverse-Sorted"]

print("Performance Analysis of Quicksort")
print("-" * 40)

# Test each size and input type
for size in sizes:
    for array_type in array_types:
        array = generate_array(size, array_type)

        # Measure deterministic Quicksort
        start_time = time.time()
        quicksort(array)
        end_time = time.time()
        print(f"Deterministic ({array_type}, size={size}): {end_time - start_time:.5f} seconds")

        # Measure randomized Quicksort
        start_time = time.time()
        randomized_quicksort(array)
        end_time = time.time()
        print(f"Randomized ({array_type}, size={size}): {end_time - start_time:.5f} seconds")

        print("-" * 40)

