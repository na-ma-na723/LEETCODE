class Solution:
    def maximum69Number (self, num: int) -> int:
        l = []
        while num>0:
            l.append(num%10)
            num = num//10
        l.reverse()
        for i in range(len(l)):
            if( l[i] == 6 ):
                l[i] = 9
                break
        for i in l:
            num = num*10 + i
        return num