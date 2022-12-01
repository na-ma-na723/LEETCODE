class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = b = i = 0
        mid = len(s)//2
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while( mid < len(s) ):
            if( s[i] in vowel ): a+=1
            if( s[mid] in vowel ): b+=1
            i+=1
            mid+=1
        if( a == b ): return True
        return False