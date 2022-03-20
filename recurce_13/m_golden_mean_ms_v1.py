# M. Золотая середина
# ID успешной посылки сортировка слиянием не проходит по времени


def merge(array, northern_part, southern_part):
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


def print_array(result):
    result = int(result) if result == float(int(result)) else result
    print(result)


def read_input():
    n = int(input())
    m = int(input())
    northern_part = [int(element) for element in input().strip().split()]
    southern_part = [int(element) for element in input().strip().split()]
    array = [''] * (m + n)
    return(array, northern_part, southern_part)


if __name__ == '__main__':
    array, northern_part, southern_part = read_input()
    print_array(get_median(merge(array, northern_part, southern_part)))
