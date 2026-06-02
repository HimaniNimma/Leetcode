class MyCircularQueue:
    def __init__(self, k: int):
        self.q=[0]*k
        self.f=0
        self.r=0
        self.c=0
        self.k=k
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.r]=value
        self.r=(self.r+1)%self.k
        self.c+=1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.f=(self.f+1)%self.k
        self.c-=1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.f]
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.r-1)%self.k]
    def isEmpty(self) -> bool:
        return self.c==0  
    def isFull(self) -> bool:
        return self.c==self.k 
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()