class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        n=len(accounts)
        for i in range(n):
            curr_sum=sum(accounts[i])
            if max_wealth<curr_sum:
                max_wealth=curr_sum
        return max_wealth