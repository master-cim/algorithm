# O. Разность треш-индексов
# ID успешной посылки не идет по памяти


def diff_index(numb, square):
    diff = []
    while square != []:
        i = square.pop()
        for j in square:
            diff.append(abs(j-i))
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


def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


def quick_sort(arr, low, high):
    '''Отсортировать список методом быстрой сортировки'''
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
        return arr


def get_position(arr, k_position):
    return(arr[k_position-1])


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    diff = diff_index(numb, square)
    len_arr = len(diff) - 1
    if len_arr >= 1000:
        print(get_position(quick_sort(diff, 0, len_arr), k_position))
    else:
        print(get_position(counting_sort(diff), k_position))
