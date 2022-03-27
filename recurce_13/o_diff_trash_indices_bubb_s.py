# O. Разность треш-индексов
# ID успешной посылки


def bubble_sort():
    _ = int(input())
    nums = [int(element) for element in input().strip().split()]
    k_position = int(input())
    diff = []
    while nums != []:
        i = nums.pop()
        for j in nums:
            diff.append(abs(j-i))
            diff.sort()
    print(diff[k_position-1])


if __name__ == '__main__':
    bubble_sort()

