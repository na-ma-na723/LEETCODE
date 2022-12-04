class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        cur = 0
        n = len(nums)
        curMin = 99999999999
        minIndex = 0
        for i in range(len(nums)-1):
            cur = cur + nums[i]
            temp = abs(cur//(i+1) - (totalSum - cur)//(n-i-1))
            if( temp < curMin ):
                curMin = temp
                minIndex = i
        temp = totalSum//n
        if( temp < curMin ):
            curMin = temp
            minIndex = n-1
        return minIndex
        
            