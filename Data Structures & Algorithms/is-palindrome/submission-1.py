class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:                      
            if not st[left].isalnum():
                left += 1
            elif not st[right].isalnum():
                right -= 1
            elif st[left] != st[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
