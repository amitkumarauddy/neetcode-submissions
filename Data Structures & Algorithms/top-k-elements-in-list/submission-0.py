class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = [[] for i in range(len(nums) + 1)]

        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i,0) + 1

        for key, value in dict1.items():
            list1[value].append(key)
        
        res = []

        for i in range(len(list1)-1, 0, -1):
            for j in list1[i]:
                res.append(j)
                if len(res) == k:
                    return res