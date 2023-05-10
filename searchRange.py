# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# def searchRange(nums, target):
#   left_most = -1
#   right_most = -1

#   left, right = 0, len(nums) - 1
#   left_2, right_2 = 0, len(nums) - 1

#   while left <= right:
#     mid = left + (right - left) // 2
#     if nums[mid] < target:
#       left = mid + 1
#     elif nums[mid] > target:
#       right = mid - 1
#     else:
#       if mid - 1 >= 0:
#         if nums[mid - 1] != target:
#           left_most = mid
#           break;
#         else:
#           right = mid - 1
#           if left == right:
#             left_most = right
#             break;
#       else:
#           left_most = mid
#           break;

#   while left_2 <= right_2:
#     mid_2 = left_2 + (right_2 - left_2) // 2
#     if nums[mid_2] < target:
#       left_2 = mid_2 + 1
#     elif nums[mid_2] > target:
#       right_2 = mid_2 - 1
#     else:
#       if mid_2 + 1 <= len(nums) - 1:
#         if nums[mid_2 + 1] != target:
#           right_most = mid_2
#           break;
#         else:
#           left_2 = mid_2 + 1
#           if left_2 == right_2:
#             right_most = left_2
#             break;
#       else:
#         right_most = mid_2
#         break;

#   return [left_most, right_most]

# print(searchRange([1,1,2], 1))

def findBound(nums, target, isFirst):

    N = len(nums)
    begin, end = 0, N - 1
    while begin <= end:
        mid = int((begin + end) / 2)

        if nums[mid] == target:

            if isFirst:
                # This means we found our lower bound.
                if mid == begin or nums[mid - 1] < target:
                    return mid

                # Search on the left side for the bound.
                end = mid - 1
            else:

                # This means we found our upper bound.
                if mid == end or nums[mid + 1] > target:
                    return mid

                # Search on the right side for the bound.
                begin = mid + 1

        elif nums[mid] > target:
            end = mid - 1
        else:
            begin = mid + 1

    return -1


def searchRange(nums, target):
    lower_bound = findBound(nums, target, True)
    if (lower_bound == -1):
        return [-1, -1]

    upper_bound = findBound(nums, target, False)

    return [lower_bound, upper_bound]
