# K. Сортировка слиянием
# ID успешной посылки


def merge(array, left_subarr, right_subarr):
    i = j = k = 0
    # Copy data to temp arrays left_subarr[] and right_subarr[]
    while i < len(left_subarr) and j < len(right_subarr):
        if left_subarr[i] < right_subarr[j]:
            array[k] = left_subarr[i]
            i += 1
        else:
            array[k] = right_subarr[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left_subarr):
        array[k] = left_subarr[i]
        i += 1
        k += 1

    while j < len(right_subarr):
        array[k] = right_subarr[j]
        j += 1
        k += 1


def merge_sort(array, left_subarr, mid, right_subarr):
    if len(array) > 1:

        # Finding the mid of the array
        # mid = len(array)//2

        # Dividing the array elements
        left_subarr = array[:mid]

        # into 2 halves
        right_subarr = array[mid:]

        # Sorting the first half
        merge_sort(left_subarr)

        # Sorting the second half
        merge_sort(right_subarr)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


def print_sorted_arr(array):
    for i in range(len(array)):
        print(array[i], end=' ')
    print()


# Driver Code
if __name__ == '__main__':
    array = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_sorted_arr(array)
    merge_sort(array)
    print("Sorted array is: ", end="\n")
    print_sorted_arr(array)
