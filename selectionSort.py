# Function to find the index of the smallest element in a list
def findSmallest(arr):
    smallest_index = 0
    smallest = arr[0]

    # Iterate through the elements starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is smaller than the current smallest
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    # Return the index of the smallest element
    return smallest_index

# Function to perform Selection Sort on a list
def selectionSort(arr):
    # Initialize an empty list to store the sorted elements
    newArr = []

    # Iterate through the elements of the input list
    for i in range(len(arr)):
        # Find the index of the smallest element in the current state of the list
        smallest = findSmallest(arr)

        # Remove the smallest element from the original list and append it to newArr
        newArr.append(arr.pop(smallest))

    # Return the sorted list
    return newArr

# Example usage of selectionSort with an unsorted list
unsorted_list = [5, 3, 6, 2, 10]
sorted_list = selectionSort(unsorted_list)

# Print the sorted list
print(sorted_list)
