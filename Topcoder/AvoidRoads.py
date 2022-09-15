# Link: https://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709
class AvoidRoads:
    def numWays(self, width, height,bad):
        blocked = set()
        for string in bad:
            string = string.replace(" ", "")
            blocked.add(string)
        
    
        dp = [[0 for i in range(height + 1)] for j in range(width + 1)]
        dp[0][0] = 1
        
        for i in range(height + 1):
            for j in range(width + 1):
                
                if i == 0 and j == 0: 
                    continue

                left_segment1 = str(j) + str(i) + str(j - 1) + str(i) if j > 0 else 0
                left_segment2 = str(j - 1) + str(i) + str(j) + str(i)  if j > 0 else 0
                bottom_segment1  = str(j) + str(i) + str(j) + str(i - 1) if i > 0 else 0
                bottom_segment2  = str(j) + str(i - 1)  + str(j) + str(i) if i > 0 else 0
                
                dp[j][i] = (dp[j - 1][i] if j  > 0 and left_segment1 not in blocked and left_segment2 not in blocked  else 0)  + (dp[j][i - 1] if i > 0 and bottom_segment1 not in blocked and bottom_segment2 not in blocked  else 0) # left + bottom

        return dp[j][i]
