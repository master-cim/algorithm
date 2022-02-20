from typing import List, Tuple


def get_close_empty_section(n: int, section: Tuple[int]) -> Tuple[int]:
    list_zero_index = [i for i in range(n) if section[i] == 0]
    return list_zero_index


def reshenie(n: int, list_zero: Tuple[int]) -> List[int]:
    result = []
    index = 0
    while index < n:
        list_distance = []
        for k in range(0, len(list_zero)):
            list_distance.append([abs(m-list_zero[k]) for m in range(0, n)])
        result.append(min([item[index] for item in list_distance]))
        index += 1
    return result


def read_input() -> Tuple[int, Tuple[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, section = read_input()
print(" ".join(map(str, reshenie(n, get_close_empty_section(n, section)))))
