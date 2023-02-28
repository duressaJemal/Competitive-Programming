class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        
        count = defaultdict(int)
        total_num = 0
        max_length = 0
        
        left = 0
        
        for right in range(n):
            
            # add
            count[s[right]] += 1
            total_num += 1
            
            # find the largest
            largest = 0
            for key in count:
                largest = max(largest, count[key])
            
            # validate
            while total_num - largest > k:
                count[s[left]] -= 1
                total_num -= 1
                left += 1
            
            # record
            max_length = max(max_length, total_num)
        
        return max_length
        
            
            
        