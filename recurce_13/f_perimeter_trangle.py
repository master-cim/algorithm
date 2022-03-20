# F. Периметр треугольника
# ID успешной посылки 66241622


def perimeter(number_section, len_section):
    list_perimetrs = []
    for i in range(number_section-2):
        if (len_section[i] <= len_section[i + 1] <= len_section[i + 2]
            and len_section[i + 2] < len_section[i] + len_section[i + 1]):
            list_perimetrs.append(
                len_section[i] + len_section[i + 1] + len_section[i + 2])
        else:
            i += 1
    return(max(list_perimetrs))


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


def read_input():
    number_section = int(input())
    len_section = [int(x) for x in input().split()]
    start = 0
    end = number_section - 1
    quick_sort(start, end, len_section)
    return(number_section, len_section)


if __name__ == '__main__':
    number_section, len_section = read_input()
    print(perimeter(number_section, len_section))
