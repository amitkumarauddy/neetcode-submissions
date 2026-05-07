class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            if heights[left] > heights[right]:
                curr_area = (right - left) * heights[right]
                right -= 1
            else:
                curr_area = (right - left) * heights[left]
                left += 1
            
            max_area = max(max_area, curr_area)


        return max_area