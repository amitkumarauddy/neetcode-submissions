class Solution:
    def search(self, nums: List[int], target: int) -> int:
        stack = []
        i = 0
        while i < len(nums):
            if nums[i]== target:
                return i
            i += 1
        return -1
    