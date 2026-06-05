from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        radient=deque()
        dire=deque()
        for i in range(n):
            if senate[i]=='R':
                radient.append(i)
            else:
                dire.append(i)
        while radient and dire:
            r=radient.popleft()
            d=dire.popleft()
            if r<d:
                radient.append(r+n)
            else:
                dire.append(d+n)
        if radient:
            return "Radiant"
        else:
            return "Dire"