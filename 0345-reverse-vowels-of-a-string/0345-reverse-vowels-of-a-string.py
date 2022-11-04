class Solution:
    def reverseVowels(self, s: str) -> str:
        el =[]
        vowel = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        for i in s:
            el.append(i)
        l = 0
        r = len(el)-1
        
        while( l <= r ):
            if( el[l] in vowel and el[r] in vowel ):
                el[l],el[r] = el[r], el[l]
                l+=1
                r-=1
            elif( el[l] in vowel ):
                r-=1
            elif( el[r] in vowel ):
                l+=1
            else:
                l+=1
                r-=1
        return "".join(el)