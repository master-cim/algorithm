from typing import List


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    result = 0
    if n != 1:
        print(temperatures)
        for c in range(1, n-1):
            if ((temperatures[c] > temperatures[c+1] and
                temperatures[c] > temperatures[c-1]) or
                (temperatures[c] < temperatures[c+1] and
                 temperatures[c] < temperatures[c-1])):
                result += 1
        return result
    else:
        result += 1
        return result


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures


n, temperatures = read_input()
print(get_weather_randomness(n, temperatures))
