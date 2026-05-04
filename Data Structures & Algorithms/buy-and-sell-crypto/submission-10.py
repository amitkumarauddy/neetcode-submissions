class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        max_pr = 0
        while left < len(prices) - 1 and right < len(prices):
            curr = prices[right] - prices[left]
            max_pr =max(max_pr, curr)
            if prices[left] > prices[right]:
                left += 1
            else:
                right += 1
        return max_pr
