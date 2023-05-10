# https://leetcode.com/problems/maximum-subarray/description?envType=study-plan&id=data-structure-i

from typing import List


def maxSubArray(self, nums: List[int]) -> int:
  max_sum = nums[0]
  current_sum = 0
  for num in nums:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)
  return max_sum
