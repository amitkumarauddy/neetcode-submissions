class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d1 = {}

        for i,j in enumerate(nums):
            d1[j] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d1 and d1[diff] != i:
                return [i,d1[diff]]
        