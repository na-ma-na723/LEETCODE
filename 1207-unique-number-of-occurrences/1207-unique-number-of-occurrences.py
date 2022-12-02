class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for i in arr:
            if( i not in m ): m[i] = 1
            else: m[i]+=1
        l = list(m.values())
        temp = set()
        for i in l:
            if( i in temp ):
                return False
            else:
                temp.add(i)
        return True