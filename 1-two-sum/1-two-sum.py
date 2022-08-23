class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if( nums[i] + nums[j] == target ):
        #             return [i,j]
        m = {}
        for i,el in enumerate(nums):
            if target-el in m:
                return [ m[target-el], i]
            m[el] = i