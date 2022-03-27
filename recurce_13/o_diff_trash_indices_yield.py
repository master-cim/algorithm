# O. Разность треш-индексов
# ID успешной посылки


def subtraction_items(square):
    while square != []:
        i = square.pop()
        for item in square:
            yield item - i


def bubble_sort():
    _ = int(input())
    nums = [int(element) for element in input().strip().split()]
    k_position = int(input())
    diff = []
    subtraction_items(nums)
    while nums != []:
        i = nums.pop()
        for j in nums:
            diff.append(abs(j-i))
        diff.sort()
    print(diff[k_position-1])


if __name__ == '__main__':
    bubble_sort()
