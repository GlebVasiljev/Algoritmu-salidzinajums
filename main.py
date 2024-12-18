import random
import time

def bubble_sort(arr):
    """
    Function to perform bubble sort on a given list.
    :param arr: List of elements to be sorted
    """
    n = len(arr)  # Get the number of elements in the list
    
    # Outer loop to traverse through all elements in the array
    for i in range(n):
        # This flag helps to optimize the algorithm by stopping early if the list is already sorted
        swapped = False
        
        # Inner loop to perform comparisons and swaps for the current pass
        # Each pass moves the largest unsorted element to the correct position
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap occurred
        
        # If no elements were swapped during the inner loop, the list is sorted
        if not swapped:
            break  # Exit the loop early for better performance

    return arr

def insertion_sort(arr):
    """
    Function to perform insertion sort on a given list.
    :param arr: List of elements to be sorted
    """
    n = len(arr)
    for i in range(1, n):
        # The current element to be inserted
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than `key`,
        # one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the `key` in its correct position
        arr[j + 1] = key

def measure_sort_times():
    """
    Measures and compares the time taken by Bubble Sort, Insertion Sort, 
    and Python's built-in sorted() function for arrays of sizes 10^i.
    """
    sizes = [10**i for i in range(2, 6)]  # Sizes: 10^2, 10^3, 10^4, 10^5
    print(f"{'Size':<10}{'Bubble Sort (s)':<20}{'Insertion Sort (s)':<20}{'Built-in Sort (s)':<20}")
    print("-" * 70)

    for size in sizes:
        # Generate a random list of the given size
        test_array = [random.randint(1, 10000) for _ in range(size)]

        # Measure time for Bubble Sort
        bubble_array = test_array[:]  # Create a copy of the array
        start_time_bubble = time.time()
        bubble_sort(bubble_array)
        end_time_bubble = time.time()

        # Measure time for Insertion Sort
        insertion_array = test_array[:]  # Create a copy of the array
        start_time_insertion = time.time()
        insertion_sort(insertion_array)
        end_time_insertion = time.time()

        # Measure time for Built-in Sort
        builtin_array = test_array[:]  # Create a copy of the array
        start_time_builtin = time.time()
        builtin_sorted_array = sorted(builtin_array)
        end_time_builtin = time.time()

        # Print results for this size
        print(f"{size:<10}{end_time_bubble - start_time_bubble:<20.5f}"
              f"{end_time_insertion - start_time_insertion:<20.5f}"
              f"{end_time_builtin - start_time_builtin:<20.5f}")

# Run the function
if __name__ == "__main__":
    measure_sort_times()