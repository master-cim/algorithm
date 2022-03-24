# O. Разность треш-индексов
# ID успешной посылки


def bubble_sort(nums):
    diff = []
    while nums != []:
        i = nums.pop()
        for j in nums:
            diff.append(abs(j-i))
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(diff) - 1):
            if diff[i] > diff[i + 1]:
                diff[i], diff[i + 1] = diff[i + 1], diff[i]
                swapped = True
    return(diff)


def read_input():
    _ = int(input())
    nums = [int(element) for element in input().strip().split()]
    k_position = int(input())
    return nums, k_position


if __name__ == '__main__':
    nums, k_position = read_input()
    print(bubble_sort(nums)[k_position-1])

