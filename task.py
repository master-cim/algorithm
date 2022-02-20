from typing import List, Tuple


def get_close_empty_section(n: int, section: Tuple[int], ) -> List[int]:
    result = []
    index = 0
    distance = []
    list_distance = []
    list_zero_index = [i for i in range(n) if section[i] == 0]
    len_z_list = len(list_zero_index)
    while index < n:
        for k in range(0, len_z_list):
            distance = abs(list_zero_index[k]-index)
            list_distance.append(distance)
            min_distance = min([list_distance[i] for i in range(0, n)])
        print(min_distance)
        result.append(min_distance)
        index += 1
    print(result.__sizeof__())
    return result


def read_input() -> Tuple[int, Tuple[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, section = read_input()
print(" ".join(map(str, get_close_empty_section(n, section))))
