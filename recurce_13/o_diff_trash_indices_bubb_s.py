# O. Разность треш-индексов
# ID успешной посылки


def bubble_sort():
    _ = int(input())
    nums = input().split()
    k_position = int(input())
    diff = []
    while nums != []:
        i = nums.pop()
        for j in nums:
            diff.append(abs(int(j)-int(i)))
        diff.sort()
    print(diff[k_position-1])


if __name__ == '__main__':
    bubble_sort()

