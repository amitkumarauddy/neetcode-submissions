class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) 
        m = len(nums2) 
        k = 0
        l = 0
        new = []
        while k < n and l < m:
            if nums1[k] < nums2[l]:
                new.append(nums1[k])
                k += 1
            else:
                new.append(nums2[l])
                l += 1

        while k < n :
            new.append(nums1[k])
            k += 1
        
        while l < m :
            new.append(nums2[l])
            l += 1

        p = len(new)
        if p % 2 == 1:
            return new[((p+1)//2)-1]
        else:
            return ((new[((p+1)//2)-1] + new[p//2]) / 2)