from typing import List


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    result = 0
    for i in range(0, n):
        print(temperatures[i])
        if i == n:
            result += 1
        # if temperatures[i+1]-temperatures[i] > 1:
        # # print(start)
        #     result += 1
            return result


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures


n, temperatures = read_input()
print(get_weather_randomness(n, temperatures))
