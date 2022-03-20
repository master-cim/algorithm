# M. Золотая середина
# ID успешной посылки быстра сортировка не проходит по времени


def combine_sub_arr(array, northern_part, southern_part):
    i = j = k = 0
    while i < len(northern_part) and j < len(southern_part):
        if northern_part[i] < southern_part[j]:
            array[k] = northern_part[i]
            i += 1
        else:
            array[k] = southern_part[j]
            j += 1
        k += 1
    while i < len(northern_part):
        array[k] = northern_part[i]
        i += 1
        k += 1
    while j < len(southern_part):
        array[k] = southern_part[j]
        j += 1
        k += 1
    return array


def get_median(array):
    len_array = len(array)
    if len_array % 2 != 0:
        return array[len_array//2]
    else:
        return(array[len_array//2] + array[len_array//2 - 1])/2


def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end


def quick_sort(start, end, array):
    if (start < end):
        part_index = partition(start, end, array)
        quick_sort(start, part_index - 1, array)
        quick_sort(part_index + 1, end, array)


def print_array(result):
    result = int(result) if result == float(int(result)) else result
    print(result)


def read_input():
    n = int(input())
    m = int(input())
    northern_part = [int(element) for element in input().strip().split()]
    southern_part = [int(element) for element in input().strip().split()]
    start = 0
    quick_sort(start, n - 1, northern_part)
    quick_sort(start, m - 1, southern_part)
    array = [''] * (m + n)
    return(array, northern_part, southern_part)


if __name__ == '__main__':
    array, northern_part, southern_part = read_input()
    print_array(get_median(
        combine_sub_arr(array, northern_part, southern_part)))
