# M. Золотая середина
# ID успешной посылки сортировка подсчетом


def counting_sort(array):
    output = [0 for i in range(len(array))]
    max_value = max(array)
    t = max_value + 1
    count = [0] * t
    for i in range(len(array)):
        count[array[i]] += 1
    k = count[0]
    for i in range(1, t):
        if (count[i] > k):
            k = count[i]
    for i in range(1, t):
        count[i] = count[i] + count[i - 1]
    for i in range(len(array)):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1


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
