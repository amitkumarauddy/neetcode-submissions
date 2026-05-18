class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = [[] for i in range(len(nums) + 1)]
        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i,0) + 1
        
        for key, values in dict1.items():
            res[values].append(key)
        
        ans = []
        for i in range(len(res) - 1, -1, -1):
            for num in res[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
