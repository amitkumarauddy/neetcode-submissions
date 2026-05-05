class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rm_dup = set(nums)

        if len(nums) == len(rm_dup):
            return False
        else:
            return True