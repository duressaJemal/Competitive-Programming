# Link: https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493

class ZigZag:
    def longestZigZag(self, sequence):
        
        n = len(sequence)
        
        diff = [0] * (n - 1)
        for i in range(n - 1):
            # diff[i] = 1 if sequence[i + 1] - sequence[i] > 0 else -1
            diff[i] = sequence[i + 1] - sequence[i]
        

        if not len(diff): return 1
        
        longest = 0

        dp = [0] * len(diff)
        dp[0] = 1

        for i in range(1,len(diff)):
            for j in range(i - 1, -1, -1):
                if diff[i] * diff[j] < 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if not dp[i]: dp[i] += 1
            longest = max(longest, dp[i])

        return longest + 1
