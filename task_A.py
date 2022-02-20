from typing import List, Tuple


def get_close_empty_section(n: int, section: List[int], ) -> List[int]:
    list_zero_index = []
    distance = []
    list_distance = []
    min_distance = []
    result = []
    for i in range(0, n):
        if section[i] == 0:
            list_zero_index.append(i)
        print(list_zero_index.__sizeof__())
    for k in range(0, len(list_zero_index)):
        distance = [abs(m-list_zero_index[k]) for m in range(0, n)]
        list_distance.append(distance)
        print(list_distance.__sizeof__())
    for index in range(0, n):
        min_distance = min([item[index] for item in list_distance])
        result.append(min_distance)
        print(result.__sizeof__())

    return result


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, section = read_input()
print(" ".join(map(str, get_close_empty_section(n, section))))
