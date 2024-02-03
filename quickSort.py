array = [9, 1, 8, 5, 4, 2]

# pass the array to the func
def quickSort(array):
    # base case if the array has 1 or 0 elements
    if len(array) < 2:
        return array
    else:
        # recursive case 
        pivot = array[0]
        # sub array for elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub array for elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        # sum up all the partitions with the specific pivot
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort(array))