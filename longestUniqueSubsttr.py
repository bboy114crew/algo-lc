# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Brute-force approach
def check(s, start, end):
  chars = set()
  for i in range(start, end + 1):
      c = s[i]
      if c in chars:
          return False
      chars.add(c)
  return True
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(s, i, j):
                res = max(res, j - i + 1)
    return res

def longestUniqueSubsttr(string):

    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # starting the initial point of window to index 0
    start = 0

    for end in range(len(string)):

        # Checking if we have already seen the element or not
        if string[end] in seen:

            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)

        # Updating the last seen value of the character
        seen[string[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length

longestUniqueSubsttr("abcabcbb")
