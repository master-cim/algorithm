# A. Поиск в сломанном массиве
# ID успешной посылки 66234615

def broken_search(nums, target) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        mid = (left_border + right_border) // 2
        if nums[mid] == target:
            return mid
        if nums[left_border] <= nums[mid]:
            if nums[left_border] <= target < nums[mid]:
                right_border = mid - 1
            else:
                left_border = mid + 1
        else: 
            if nums[mid] < target <= nums[right_border]:
                left_border = mid + 1
            else:
                right_border = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
