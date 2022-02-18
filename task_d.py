from typing import List


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    result = 0
    if n != 1:
        day = [temperatures[i]-temperatures[i-1] for i in range(
            1, len(temperatures))]
        if day[0] < 0:
            result += 1
        if day[n-2] > 0:
            result += 1
        for c in range(1, n-1):
            if (temperatures[c] > temperatures[c+1] and
               temperatures[c] > temperatures[c-1]):
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
