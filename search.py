# https://leetcode.com/problems/search-in-rotated-sorted-array

def binary_search(left, right, nums, target):
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        else:
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
    return -1

def find_rotate_index(nums):
    left = 0
    right = len(nums) - 1

    if len(nums) < 2 or nums[left] < nums[right]:
        return 0

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        else:
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

def search(nums, target):
    rotate_index = find_rotate_index(nums)

    if nums[rotate_index] == target:
        return rotate_index

    # if array is not rotated, search in the entire array
    if rotate_index == 0:
        return binary_search(0, len(nums) - 1, nums, target)

    if target < nums[0]:
        return binary_search(rotate_index, len(nums) - 1, nums, target)
    else:
        return binary_search(0, rotate_index - 1, nums, target)


print(search([1], 0))
