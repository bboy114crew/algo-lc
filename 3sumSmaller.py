# https://leetcode.com/problems/3sum-smaller

def twoSumII(nums, i, target):
    sum = 0
    lo, hi = i + 1, len(nums) - 1
    rest = target - nums[i]

    while (lo < hi):
        current_sum = nums[lo] + nums[hi]
        if current_sum < rest:
            sum += hi - lo
            lo += 1
        else:
            hi -= 1
    return sum


def threeSumSmaller(nums, target):
    nums.sort()
    sum = 0
    for i in range(len(nums)):
        sum += twoSumII(nums, i, target)
    return sum


print(threeSumSmaller([-2,0,1,3], 2))
