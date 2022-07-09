# link: https://leetcode.com/problems/longest-repeating-character-replacement/

# time: O(n * 26)
# space: O(n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        store = {}
        start, end, longest = 0, 0, 0
        
        while end < n:
            store[s[end]] = 1 + store.get(s[end], 0)
            while (end - start + 1) - max(store.values()) > k:
                store[s[start]] -= 1
                start += 1
            longest = max(longest, end - start + 1)
            end += 1
        return longest

# CHECK OUT THE OPTIMIZED SOLUTION
