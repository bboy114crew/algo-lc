def searchInsert(nums, target) -> int:
  left, right = 0, len(nums) - 1
  while left <= right:
    pivot = (left + right) // 2
    if nums[pivot] == target:
      return pivot
    if target < nums[pivot]:
      right = pivot - 1
    else:
      left = pivot + 1
  return left

def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
    return result

print(sortedSquares([-3, -2, -1, 4, 5, 6]))
