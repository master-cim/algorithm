from typing import List, Tuple


def distance_one_way(house_list):
    last_null = -1
    one_way_list = [0] * n
    for null_number in range(0, n):
        if house_list[null_number] == '0':
            for house_number in range(last_null + 1, null_number):
                one_way_list[house_number] = abs(house_number-null_number)
            last_null = int(null_number)
    if last_null < n:
        for house_number in range(last_null+1, n):
            one_way_list[house_number] = float("inf")
    return one_way_list


def distance_two_way(house_list):
    forward = distance_one_way(house_list)
    backward = distance_one_way(house_list[::-1])
    final_list = [min(forward_dist, back_dist)
                  for forward_dist, back_dist in zip(forward, backward[::-1])]
    final_list = [str(distance) for distance in final_list]
    return final_list
  

def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    section = list(map(int, input().strip().split()))
    return n, section


n, house_list = read_input()
print(" ".join(distance_two_way(house_list)))
