class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_diff = 0

        left = 0

        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                curr_diff = prices[right] - prices[left]
                max_diff = max(curr_diff, max_diff)
            else:
                left = right
            right += 1
        
        return max_diff