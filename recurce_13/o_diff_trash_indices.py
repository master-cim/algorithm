# O. Разность треш-индексов
# ID успешной посылки


def diff_index(numb, square):
    diff = [''] * (numb * (numb-1) // 2)
    idx = 0
    while square != []:
        i = square.pop()
        for j in square:
            diff[idx] = abs(j-i)
            idx += 1
    return(diff)


def counting_sort(arr):
    '''Отсортировать список методом подсчета'''
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    return arr


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:len(array)])
    i = r = k = 0
    while i < len(left) and r < len(right):
        if left[i] < right[r]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[r]
            r += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while r < len(right):
        array[k] = right[r]
        r += 1
        k += 1
    return array


def merge(sub_arrays):
    '''Отсортировать список методом слияния'''
    print('Отсортировать список методом слияния')
    array = [''] * (numb * (numb-1) // 2)
    left_part = merge_sort(sub_arrays[0])
    right_part = merge_sort(sub_arrays[1])
    i = j = k = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            array[k] = left_part[i]
            i += 1
        else:
            array[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        array[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        array[k] = right_part[j]
        j += 1
        k += 1
    return array


def get_position(arr, k_position):
    return(arr[k_position-1])


def func_chunks_generators(lst, n):
    for x in range(0, len(lst), n):
        e_c = lst[x: n + x]
        yield e_c


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    diff = diff_index(numb, square)
    len_arr = len(diff)
    if len_arr >= 10:
        sub_arrays = list(func_chunks_generators(diff, len_arr//2))
        print(get_position(merge(sub_arrays), k_position))
    else:
        print(get_position(counting_sort(diff), k_position))
