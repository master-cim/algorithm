# A. Мониторинг
# ID успешной посылки 65624070

from typing import List, Tuple


def transporate(n: int, m: int, matrix: List[int]) -> List[int]:
    idx_m = 0
    while idx_m < m:
        result = []
        idx_n = 0
        while idx_n < n:
            result.append(matrix[idx_n][idx_m])
            idx_n += 1
        idx_m += 1
        print_array(result)


def read_input() -> Tuple[int, int, List[List[int]]]:
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return n, m, matrix


def print_array(result: List[int]):
    print(" ".join(map(str, result)))


n, m, matrix = read_input()
transporate(n, m, matrix)
