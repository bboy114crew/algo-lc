from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
  store = dict()
  for num in nums:
    if num in store:
      return True
    else:
      store[num] = True
  return False
