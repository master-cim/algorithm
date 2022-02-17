from typing import List, Tuple


def get_neighbours(n: int, m: int, matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    if row != n-1:
        down = (matrix[row+1])[col]
        result.append(down)
    if col != m-1:
        right = (matrix[row])[col+1]
        result.append(right)
    if row != 0:
        up = (matrix[row-1])[col]
        result.append(up)
    if col != 0:
        left = (matrix[row])[col-1]
        result.append(left)
    result = sorted(result)
    return(result)


def read_input() -> Tuple[int, int, List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return n, m, matrix, row, col


n, m, matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(n, m, matrix, row, col))))
