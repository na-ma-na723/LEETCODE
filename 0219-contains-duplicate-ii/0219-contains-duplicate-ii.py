class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i,x in enumerate(nums):
            if x in m and ( i - m[x] <= k ): return True
            m[x] = i
        return False