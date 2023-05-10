function findLongestSubstring(str) {
  let longest = 0;
  let seen = {};
  let start = 0;

  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (seen[char]) {
      start = Math.max(start, seen[char]);
    }
    // index - beginning of substring + 1 (to include current in count)
    longest = Math.max(longest, i - start + 1);
    // store the index of the next char so as to not double count
    seen[char] = i + 1;
  }
  return longest;
}

const findLongestSubstring = function(str) {
  let store = {}
  let count = 0
  let left  = 0
  let max = 0

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    const location = store[char];
    if (typeof location === 'undefined') {
      count += 1
      if (i === str.length - 1) {
        max = Math.max(count, max)
        return max
      }
    } else {
      if (store[char] < left) {
        count += 1
        if (i === str.length - 1) {
          max = Math.max(count, max)
          return max
        }
      } else {
        max = Math.max(count, max)
        left = store[char] + 1
        count = i - store[char]
      }
    }
    store[char] = i
  }

  return max
};

console.log(findLongestSubstring(''))
