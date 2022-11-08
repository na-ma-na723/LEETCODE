class Solution:
    def makeGood(self, s: str) -> str:
        lis = []
        for i in range(0,len(s)):
            if len(lis) == 0:
                lis.append(s[i])
            elif abs( ord(s[i]) - ord(lis[-1]) ) == 32:
                lis.pop(-1)
            else: 
                lis.append(s[i])
        return "".join(lis)