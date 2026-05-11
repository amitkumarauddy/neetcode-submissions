class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # -4,-1,-1,0,1,2
        for i,j in enumerate(nums):
            if j > 0:
                break

            if  i > 0 and j == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            target = 0
            while l < r:
                three_sum = j + nums[l] + nums[r]

                if three_sum < target:
                    l += 1
            
                elif three_sum > target:
                    r -= 1
            
                else:
                    res.append([j, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l < r:
                        l += 1
        
        return res