class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        count = defaultdict(int)

        for r,num in enumerate(nums):
            count[num]+=1
            while count[num]>k:
                count[nums[l]]-=1
                l+=1
            ans = max(ans,r-l+1)

        return ans

            
        
