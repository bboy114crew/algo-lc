// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

function maxSubarrSum(nums, k) {
  let curMax = 0;
  for (let i = 0; i < k; i++) {
    max += nums[i]
  }

  for (let i = k; i < nums.length; i++) {
    const newMax = curMax - nums[i - k] + a[i];
    curMax = Math.max(curMax, newMax);
  }

  return curMax
}

function maxDistinctSubarrSum(nums, k) {
  let currentSum = 0
  let maxSum = 0
  let store = new Map()
  let leftMost = 0

  for (let i = 0; i < k; i++) {
    const element = nums[i];
    if (store.get(element)) {
      store.set(element, store.get(element) + 1)
    } else {
      store.set(element, 1)
    }
    currentSum += element
  }

  if (store.size === k) {
    maxSum = currentSum
  }

  for (let i = k; i < nums.length; i++) {
    const element = nums[i];
    currentSum = currentSum - nums[leftMost] + element

    if (store.get(element)) {
      store.set(element, store.get(element) + 1)
    } else {
      store.set(element, 1)
    }

    if (store.get(nums[leftMost])) {
      store.set(nums[leftMost], store.get(nums[leftMost]) - 1)
    }

    if (store.get(nums[leftMost]) === 0) {
      store.delete(nums[leftMost])
    }

    if (store.size === k) {
      maxSum = Math.max(maxSum, currentSum)
    }

    leftMost += 1
  }

  return maxSum
}

console.log(maxDistinctSubarrSum([1,1,1,7,8,9,6], 3))
