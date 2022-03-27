# O. Разность треш-индексов
# ID успешной посылки


def diff_index(arr_items):
    diff = []
    while arr_items != []:
        i = arr_items.pop()
        for j in arr_items:
            diff.append(abs(j-i))
            if len(diff) == 1:
                continue
            else:
                for i in range(1, len(diff)):
                    item_to_insert = diff[i]
                    j = i - 1
                    while j >= 0 and diff[j] > item_to_insert:
                        diff[j + 1] = diff[j]
                        j -= 1
                    diff[j + 1] = item_to_insert
    return(diff)


def read_input():
    _ = int(input())
    items = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return items, k_position


if __name__ == '__main__':
    items, k_position = read_input()
    print(diff_index(items)[k_position-1])

