class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        dt = {}
        output = 0

        for i in nums:

            if i in dt:
                dt[i] += 1
            else:
                dt[i] = 1

        for i in dt:

            if k - i in dt:

                if dt[i] == 0:
                    continue

                if k - i == i:
                    div = dt[i]//2
                    output = output + div
                    continue

                m = min(dt[i], dt[k-i])

                for value in range(m):
                    output += 1

                dt[i] -= m
                dt[k-i] -= m

        return output
