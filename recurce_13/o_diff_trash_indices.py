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


def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j-1] > val:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = val


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
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
        return arr


def hybrid_sort(arr, low, high):
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            print('быстрая сортировка')
            pivot = partition(arr, low, high)
            if pivot - low < high - pivot:
                hybrid_sort(arr, low, pivot-1)
                low = pivot + 1
            else:
                hybrid_sort(arr, pivot + 1, high)
                high = pivot-1


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
    hybrid_sort(diff, 0, len_arr)
    print(get_position(diff, k_position))

