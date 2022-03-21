# M. Золотая середина
# ID успешной посылки 66274469


def merge(array, northern_part, southern_part):
    array = sorted(northern_part + southern_part)
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
