def findMin(nums) -> int:
    l = 0
    r = len(nums) - 1
    if len(nums) < 2 or nums[l] < nums[r]:
        return nums[0]
    while l <= r:
        m = (l + r) // 2
        if m - 1 >= 0 and nums[m - 1] > nums[m]:
            return nums[m]

        if m + 1 <= len(nums) - 1 and nums[m] > nums[m + 1]:
            return nums[m + 1]

        if nums[l] < nums[m]:
            l = m + 1
        else:
            r = m - 1
    return nums[0]




print(findMin([2,3,4,5,1]))
