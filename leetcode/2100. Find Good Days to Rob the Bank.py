# link: https://leetcode.com/problems/find-good-days-to-rob-the-bank/submissions/

class Solution:
    def goodDaysToRobBank(self, A: List[int], t: int) -> List[int]:
            if t == 0: return list(range(len(A)))
            lft, rgt, n = [1], [1], len(A)

            curr = 1
            for i in range(1, n):
                if A[i] <= A[i - 1]: curr += 1
                else: curr = 1
                lft.append(curr)

            curr = 1
            for i in range(n - 2, -1, -1):
                if A[i] <= A[i + 1]: curr += 1
                else: curr = 1
                rgt.append(curr)
            rgt.reverse()

            return [i for i in range(n) if lft[i] >= t + 1 and rgt[i] >= t + 1]
        
