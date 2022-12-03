class Solution:
    def frequencySort(self, s: str) -> str:
        m = {}
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        dict_item = sorted(m.items(), key=lambda value:value[1], reverse = True)
        
        ans = ""
        for ch,i in dict_item:
            ans += ch*i
            
        return ans