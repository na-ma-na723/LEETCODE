class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        n = {}
        for i in ransomNote:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1 
        for i in magazine:
            if i not in n:
                n[i] = 1
            else:
                n[i] += 1 
        for i in ransomNote:
            if (i not in n) or ( m[i] > n[i] ):
                return False
        return True
                
                