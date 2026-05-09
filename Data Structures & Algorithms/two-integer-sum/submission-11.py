class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}

        for i,j in enumerate(nums):
            diff = target - j

            if diff in d1:
                return [d1[diff],i]
            
            else:
                d1[j] = i

        return d1