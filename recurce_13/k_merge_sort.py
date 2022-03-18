# K. Сортировка слиянием
# ID успешной посылки 66168140

def merge_sort(array, beg, end):
    if len(array) == 1:
        return array
    mid = len(array)//2
    l_subarr = array[beg:mid]
    r_subarr = array[mid:end]
    merge_sort(l_subarr, beg, end)
    merge_sort(r_subarr, beg, end)
    i = j = k = 0
    while i < len(l_subarr) and j < len(r_subarr):
        if l_subarr[i] < r_subarr[j]:
            array[k] = l_subarr[i]
            i += 1
        else:
            array[k] = r_subarr[j]
            j += 1
        k += 1
    while i < len(l_subarr):
        array[k] = l_subarr[i]
        i += 1
        k += 1
    while j < len(r_subarr):
        array[k] = r_subarr[j]
        j += 1
        k += 1
    return(array)


def merge(array, beg, mid, end):
    left_sub = array[beg:mid]
    right_sub = array[mid:end]
    left_arr = merge_sort(left_sub, beg, mid)
    right_arr = merge_sort(right_sub, 0, len(right_sub))
    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            array[k] = left_arr[i]
            i += 1
        else:
            array[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        array[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        array[k] = right_arr[j]
        j += 1
        k += 1
    return array


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()

