from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=Counter(tasks)#A:3,B:3
        max_heap=[]
        time=0
        for count in d.values():
            heapq.heappush(max_heap,-count)#[-3,-3]
        while max_heap:
            temp=[]
            cycle=n+1
            while cycle>0 and max_heap:
                count=-heapq.heappop(max_heap)#Making -ve to +ve
                count-=1
                time+=1
                if count>0:
                    temp.append(count)
                cycle-=1
            for count in temp:
                heapq.heappush(max_heap,-count)
            if max_heap:
                time+=cycle
        return time