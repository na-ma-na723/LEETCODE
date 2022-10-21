class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i,x in enumerate(nums):
            if x not in m:
                m[x]=i
            else:
                if( i - m[x] <= k ): return True
                else: m[x] = i
        return False