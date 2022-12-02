class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if( len(word1) != len(word2) ): return False
        m = {}
        n = {}
        a = set(word1)
        b = set(word2)
        for i in a:
            if( i not in b ): return False
        i = 0
        while( i < len(word1) ):
            if( word1[i] not in m ): m[word1[i]] = 1
            else: m[word1[i]] += 1
            if( word2[i] not in n ): n[word2[i]] = 1
            else: n[word2[i]] += 1
            i+=1
        w1 = sorted(list( m.values() ))
        w2 = sorted(list( n.values() ))
        if( w1 == w2 ): return True
        return False