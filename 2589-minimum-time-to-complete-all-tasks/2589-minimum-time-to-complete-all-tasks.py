class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks,key=lambda x:x[1])
        chosen_set = set()
        for task in tasks:
            cur_start,cur_end,cur_duration = task[0],task[1],task[2]
            for time in chosen_set:
                if time >= cur_start and time <=cur_end:
                    cur_duration-=1
                if cur_duration==0:
                    break
            while cur_duration>0:
                if cur_end not in chosen_set:
                    chosen_set.add(cur_end)
                    cur_duration-=1
                cur_end-=1
        return len(chosen_set)
    
    