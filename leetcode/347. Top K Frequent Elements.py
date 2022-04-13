class Solution:
    def topKFrequent(self, nums, k):

        d = {}
        output = []
        for i in nums:

            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        freqent = sorted(d.items(), key=lambda kv: (kv[1]), reverse=True)
        for i in range(k):
            output.append(freqent[i][0])

        return output
