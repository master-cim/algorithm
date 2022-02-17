from typing import List


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    result = 0
    if n != 1:
        day_prev = [temperatures[i]-temperatures[i-1] for i in range(
            1, len(temperatures))]
        print(temperatures)
        print(day_prev)
        # if day_prev[n-2] < day_prev[n-3] or day_prev[0] > day_prev[1]:
        #     result = 1
        for c in range(0, len(day_prev)-1):
            if (day_prev[c] > 1 and
                day_prev[c] > day_prev[c-1] and
                day_prev[c] > day_prev[c+1]):
                print(day_prev[c])
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
