# N. Клумбы

from functools import reduce


def comparison_f(left, right):
    sub_arr = []
    if left[1] < right[0]:
        return left
    elif (left[1] >= right[0] and left[1] < right[1]):
        sub_arr.append(left[0])
        sub_arr.append(right[1])
        return(sub_arr)
    # elif (left[1] > right[0] and left[1] <= right[1]):
    #     sub_arr.append(left[0])
    #     sub_arr.append(right[1])
    #     return(sub_arr)


def comparison(left, right):
    sub_arr = []
    if left[1] < right[0]: 
        return right
    elif (left[1] >= right[0] and left[1] < right[1]):
        sub_arr.append(left[0])
        sub_arr.append(right[1])
        return(sub_arr)
    else:
        return
    # elif (left[1] > right[0] and left[1] <= right[1]):
    #     sub_arr.append(left[0])
    #     sub_arr.append(right[1])
    #     return(sub_arr)


def flowerbed(flowerbed_coordinates):
    result = []
    result.append(comparison_f(flowerbed_coordinates[0], flowerbed_coordinates[1]))
    n = len(result)
    s = comparison(result[-n], flowerbed_coordinates[1])
    if s is not None:
        result.append(s)
    h = comparison_f(result[-n+1], result[-n])
    if h is not None:
        result.append(h)
    s = comparison(result[-n], flowerbed_coordinates[2])
    if s is not None:
        result.append(s)
    h = comparison(result[-n+1], result[-n])
    if h is not None:
        result.append(h)
    # result.append(h)
    # for item in range(1, len(flowerbed_coordinates)):
    #     print(comparison(result[-(len(result)-1)], flowerbed_coordinates[item]))
    return (result)

def read_input():
    number_gardeners = int(input())
    flowerbed_coordinates = []
    for _ in range(number_gardeners):
        flowerbed_coordinates.append(list(map(int, input().strip().split())))
    unique = reduce(lambda l, x: l+[x] if x not in l else l, flowerbed_coordinates, [])
    flowerbed_coordinates = sorted(unique)

    return flowerbed_coordinates


if __name__ == '__main__':
    flowerbed_coordinates = read_input()
    print(flowerbed_coordinates)
    print(flowerbed(flowerbed_coordinates))
    # print(*(list(zip(*flowerbed_coordinates))[0]), sep="\n")
