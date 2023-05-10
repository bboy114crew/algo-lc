# https://leetcode.com/problems/find-peak-element
# https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/mit6_006f11_lec01/
# https://www.youtube.com/watch?v=HtSuA80QTyo

# If a[n/2] < a[n/2 − 1] then only look at left half 1 . . . n/2 − − − 1 to look for peak
# Else if a[n/2] < a[n/2 + 1] then only look at right half n/2 + 1 . . . n to look for peak
# Else n/2 position is a peak: WHY?
# a[n/2] ≥ a[n/2 − 1]
# a[n/2] ≥ a[n/2 + 1]

def findPeakElement(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l

print(findPeakElement([1,2,3,1]))
