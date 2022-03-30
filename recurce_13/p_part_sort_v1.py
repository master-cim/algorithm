# P. Частичная сортировка
# ID успешной посылки

def subtraction_items(square):
    while square != []:
        i = square.pop()
        for item in square:
            yield item - i

def my_part_sort(arr):
    index_min, max_value = min(enumerate(arr), key=lambda i_v: i_v[1])
    index_max, max_value = max(enumerate(arr), key=lambda i_v: i_v[1])
    return arr[:index_min], arr[index_min:index_max], arr[index_max:]


def read_input():
    _ = int(input())
    arr = [int(element) for element in input().strip().split()]
    return arr


if __name__ == '__main__':
    arr = read_input()
    diff = []
    for it in subtraction_items(arr):
        print(it, end=" ")


