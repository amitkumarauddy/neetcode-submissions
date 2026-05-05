class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
 
        s = set(nums)
        #2,3,4,5,10,20
        longest = 0

        for i in nums:
            if (i - 1) not in s:
                length = 0                
                while (i + length) in s:
                    length += 1
                longest = max(longest, length)

        return longest