class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        n = len(nums)
        missing = (n*(n+1))//2
        duplicate = 0
        for i in nums:
            if i not in s:
                s.add(i)
                missing -= i
            else:
                duplicate = i
        return [duplicate, missing]
        