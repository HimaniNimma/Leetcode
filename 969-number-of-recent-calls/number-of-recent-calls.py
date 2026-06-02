class RecentCounter:

    def __init__(self):
        self.calls=[]
    def ping(self, t: int) -> int:
        self.calls.append(t)
        count=0
        for i in self.calls:
            if t-3000<=i<=t:
                count=count+1
        return count
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)