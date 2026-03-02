from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        ans = []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        n = len(sorted_intervals)
        i = 0
        while i < n - 1:
            curr_start = sorted_intervals[i][0]
            curr_end = sorted_intervals[i][1]
            while i + 1 < n and sorted_intervals[i+1][0] <= curr_end:
                curr_end = max(curr_end, sorted_intervals[i+1][1])
                i += 1
            ans.append([curr_start, curr_end])
            i += 1
        if i == n - 1:
            ans.append(sorted_intervals[i])
        return ans

