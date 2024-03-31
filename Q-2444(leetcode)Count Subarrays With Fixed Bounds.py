class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans= 0
        mip= map= l = -1
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                l = i
            if num == minK:
                mip= i
            if num == maxK:
                map= i
            ans += max(0, min(mip, map) - l)
            
        return ans
