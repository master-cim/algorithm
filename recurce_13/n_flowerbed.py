# N. Клумбы

from functools import reduce


def driver_add(items):
    not_hashbable = []
    hashable = set()
    for item in items:
        comparison(item, item)
        try:
            if item not in hashable:
                hashable.add(item)
                yield item
        except TypeError:
            if item not in not_hashbable:
                not_hashbable.append(item)
                yield item


def comparison_f(left, right):
    sub_arr = []
    if left[1] > right[0] and left[1] > right[1]:
        return left
    elif left[1] <= right[1] and left[1] > right[0]:
        sub_arr.append(left[0])
        sub_arr.append(right[1])
        return(sub_arr)
    elif left[1] < right[0]:
        return left


def comparison(left, right):
    sub_arr = []
    if left[1] >= right[0]:
        sub_arr
        print(left)
    elif left[1] <= right[1] and left[1] > right[0]:
        
        sub_arr.append(left[0])
        sub_arr.append(right[1])
        print(sub_arr)
    elif left[1] < right[0]:
        print(right)


def flowerbed(arr):
    # not_hashbable = []
    sub_arr = []
    hashable = set()
    for it in range(1, len(arr)):
        if arr[it-1][1] < arr[it][0] and arr[it] == arr[len(arr)-1]:
            sub_arr = arr[it]
            hashable.add(tuple(sub_arr))
        elif (arr[it-1][1] < arr[it][0]
            or (arr[it-1][1] >= arr[it][0] and arr[it-1][1] >= arr[it][1])):
            sub_arr = arr[it-1]
            print(sub_arr)
            hashable.add(tuple(sub_arr))
            print(hashable)
        elif arr[it-1][1] >= arr[it][0] and arr[it-1][1] <= arr[it][1]:
            sub_arr.append(arr[it-1][0])
            sub_arr.append(arr[it][1])
            print(sub_arr)
            # arr[it-1] = sub_arr
            # arr[it] = sub_arr
            hashable.add(tuple(sub_arr))

    return(hashable)


def test(result):
            # try:
            #     if sub_arr not in hashable:
            #         hashable.add(sub_arr)
            #         print(hashable)
            #         yield sub_arr
            # except TypeError:
            #     if sub_arr not in not_hashbable:
            #         not_hashbable.append(sub_arr)
            #         # print(not_hashbable)
            #         yield sub_arr
    return(flowerbed(result))


def read_input():
    number_gardeners = int(input())
    flowerbed_coordinates = []
    for _ in range(number_gardeners):
        flowerbed_coordinates.append(list(map(int, input().strip().split())))
    print(flowerbed_coordinates)
    unique = reduce(lambda l, x: l+[x] if x not in l else l, flowerbed_coordinates, [])
    unique.sort()
    print(unique)
    return unique


if __name__ == '__main__':
    unique = read_input()
    # print(flowerbed_coordinates)
    # print(flowerbed(flowerbed_coordinates))
    # print(flowerbed(unique))
    for i in flowerbed(unique):
        for x in i:
            print(x, end=' ')
        print(sep="\n")
    # print(*(list(zip(*flowerbed(unique)))[0]), sep="\n")
