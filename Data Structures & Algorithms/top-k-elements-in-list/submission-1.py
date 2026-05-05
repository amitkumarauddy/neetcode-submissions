class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l1 = [[] for i in range(len(nums)+1)]

        d1 = {}
        for i in nums:
            d1[i] = d1.get(i,0) + 1

        for key, value in d1.items():
            l1[value].append(key)

        res = []
        for i in range(len(l1) - 1,0, -1):
            for j in l1[i]:
                res.append(j)
            if len(res) == k:
                return res