def broken_search(nums, target) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        mid = (left_border + right_border) // 2
        if nums[mid] == target:
            return mid
        if(nums[left_border] <= target < nums[mid]
           or nums[mid] > target >= nums[right_border]):
            right_border = mid - 1
        else:
            left_border = mid + 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
