# Sorted array of numbers
array = [1,2,3,4,5,6,7,8,9,10]
item = 8

# Function takes the array and the item to search for
def binarySearch(array, item):
    # Define the start and end of the array
    low = 0
    high = len(array) - 1

    # While there isn't only one element
    while low <= high: 
        # Define the middle of the array
        mid = (low + high) // 2
        guess = array[mid]

        # If found return index, if its too high then make high start from the middle of the array -1 else if its too low start at mid + 1
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    # Item doesn't exist
    return None

print("The number is at position ", binarySearch(array, item))

# Runs O log(n) time. For example if theres 128 elements in the list it will take max 7 guesses