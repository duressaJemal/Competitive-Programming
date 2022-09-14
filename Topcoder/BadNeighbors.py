# Link: https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009

# Bottom-up

# Time: O(N)
# Space: O(N)

class BadNeighbors:
     def maxDonations(self, donations):
            def linear_donation(nums):
                left, right = 0, 0
                for num in nums:
                    temp = right
                    left = max(right, num + left)
                    right, left = left, temp
                return right
            
            return max(linear_donation(donations[:-1]), linear_donation(donations[1:]))
