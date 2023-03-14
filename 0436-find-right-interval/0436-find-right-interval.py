class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)
        
        # build hash_map
        hash_map = defaultdict(int)
        starts = []
        res = []
        
        for index in range(n):
            value = intervals[index][0]
            starts.append(value)
            hash_map[value] = index
            
        starts.sort()
        for s, end in intervals:
            index = bisect_left(starts, end)
            if index == len(starts):
                res.append(-1)
            else:
                res.append(hash_map[starts[index]])
        
        return res
        
        
        