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


def counting_sort(arr, k_position):
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
    return arr[k_position-1]


def quick_sort(diff, left, right):
    """
    Отсортировать список методом быстрой сортировки
    """
    def subpart():
        pivot_competitors = (diff[left])
        start = left + 1
        end = right - 1
        while True:
            if (start <= end and diff[end] > pivot_competitors):
                end -= 1
            elif (start <= end and diff[start] < pivot_competitors):
                start += 1
            elif ((diff[end] > pivot_competitors)
                  or (diff[start] < pivot_competitors)):
                continue
            if start <= end:
                diff[start], diff[end] = (diff[end], diff[start])
            else:
                diff[left], diff[end] = (diff[end], diff[left])
                return end
    if right - left > 1:
        pivot = subpart()
        quick_sort(diff, left, pivot)
        quick_sort(diff, pivot + 1, right)


def read_input():
    numb = int(input())
    square = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return numb, square, k_position


if __name__ == '__main__':
    numb, square, k_position = read_input()
    diff = diff_index(numb, square)
    if len(diff) > 100:
        left = 0
        print(quick_sort(diff, left, right=len(diff)))
    else:
        print(counting_sort(diff, k_position))
