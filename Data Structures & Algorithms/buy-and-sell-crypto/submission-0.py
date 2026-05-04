class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_pr = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                curr = prices[j] - prices[i]
                if max_pr < curr:
                    max_pr = curr
        
        return max_pr