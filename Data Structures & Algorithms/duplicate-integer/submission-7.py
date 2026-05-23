class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        n = len(set(nums)) 
        b =  len(nums)
        return n < b