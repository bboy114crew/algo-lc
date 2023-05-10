# https://leetcode.com/problems/3sum

# Brute-force
# def threeSum(naums):
#   nums.sort()
#   result = []
#   for i in range(len(nums)):
#     if i > 0 and nums[i] == nums[i - 1]:
#       continue
#     for j in range(i + 1, len(nums)):
#       if j > i + 1 and nums[j] == nums[j - 1]:
#         continue
#       for k in range(j + 1, len(nums)):
#         if k > j + 1 and nums[k] == nums[k - 1]:
#           continue
#         if nums[i] + nums[j] + nums[k] == 0:
#           result.append([nums[i], nums[j], nums[k]])
#   return result

res = []

def twoSumII(nums, i: int, res):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            # because array was sorted so we increment lo while the next value is the same as before to avoid duplicates in the result.
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1

def threeSum(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSumII(nums, i, res)
    return res

print(threeSum([-1,0,1,2,-1,-4]))
