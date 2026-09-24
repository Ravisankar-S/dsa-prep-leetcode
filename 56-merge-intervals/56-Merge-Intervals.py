class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result = [intervals[0]]
        
        for start,end in intervals[1:]:
            last_start,last_end = result[-1]

            if start <= last_end:
                result[-1][1] = max(end,last_end)
            else:
                result.append([start,end])

        return result