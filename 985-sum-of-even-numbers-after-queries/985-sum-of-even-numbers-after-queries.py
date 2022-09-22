def evenSum(nums):
    res = 0
    for i in nums:
        if i%2==0:
            res+=i
    return res

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even = 0
        for i in nums:
            if i%2==0:
                even+=i
        for i in queries:
            temp = nums[ i[1] ] + i[0]
            if temp%2==0:
                if nums[i[1]]%2==0:
                    diff = temp - nums[i[1]]
                    even = even + diff
                else:
                    even = even + temp
            else:
                if nums[i[1]]%2==0:
                    even = even - nums[i[1]]
            res.append(even)
            nums[i[1]] = temp
        return res