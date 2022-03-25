# O. Разность треш-индексов
# ID успешной посылки


def diff_index(items_arr, k_position):
    diff = []
    while items_arr != []:
        i = items_arr.pop()
        for j in items_arr:
            diff.append(abs(j-i))
    for i in range(1, len(diff)):
        item_to_insert = diff[i]
        j = i - 1
        while j >= 0 and diff[j] > item_to_insert:
            diff[j + 1] = diff[j]
            j -= 1
        diff[j + 1] = item_to_insert
    return(diff[k_position-1])


def read_input():
    _ = int(input())
    items_arr = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return items_arr, k_position


if __name__ == '__main__':
    items_arr, k_position = read_input()
    print(diff_index(items_arr, k_position))

