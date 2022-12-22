# Link: https://leetcode.com/problems/count-pairs-of-similar-strings/
#Q: 2506. Count Pairs Of Similar Strings

# Time: O(M*N) where M = len(words[i]), N = len(words)
# Space: O(N)

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        dic = defaultdict(int)
        for word in words:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] = 1
            w = tuple(count)
            dic[w] += 1
        
        output = 0
        for key in dic:
            output += (dic[key] * (dic[key] - 1)) // 2
        
        return output
        
