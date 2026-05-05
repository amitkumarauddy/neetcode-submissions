class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d1 = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord("a")] += 1
            
            d1[tuple(count)].append(s)
        
        return list(d1.values())