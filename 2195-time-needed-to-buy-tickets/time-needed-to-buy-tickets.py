from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        time=0
        for i in range(len(tickets)):
            q.append((i,tickets[i]))
        while q:
            index,count=q.popleft()
            count-=1
            time+=1
            if index==k and count==0:
                return time
            if count>0:
                q.append((index,count))