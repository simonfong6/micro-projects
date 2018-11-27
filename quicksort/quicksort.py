
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    print("Pivot: {}".format(pivot))

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        print(arr)

    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(arr)
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def main():
    nums = [3, 4, 5, 1, 2, 8, 9]
    print(nums)

    quickSort(nums, 0, len(nums) - 1)

    print(nums)


if __name__ == '__main__':
    main()
