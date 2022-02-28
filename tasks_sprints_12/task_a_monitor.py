# A. Мониторинг
# ID успешной посылки 

from typing import List, Tuple


def transporate(n: int, m: int, matrix: List[int]) -> List[int]:
    result = []
    idx_n = 0
    idx_m = 0
    while idx_m < m:
        while idx_n < n:
            result.append(list(matrix[idx_n][idx_m]))
            idx_n += 1
            
            print(result)
        # for item in range(len(matrix)):
        #     result.append(list(map(int, input().strip().split())))
        idx_m += 1
    return(result)


def read_input() -> Tuple[int, int, List[List[int]]]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    print(matrix)
    return n, m, matrix


n, m, matrix = read_input()
print(" ".join(map(str, transporate(n, m, matrix))))