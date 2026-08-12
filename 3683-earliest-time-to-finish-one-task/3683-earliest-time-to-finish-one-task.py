class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        earliest = float("inf")
        for s, t in tasks:
            finish = s + t
            earliest = min(earliest, finish)
        return earliest