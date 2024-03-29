class Solution:
    def countSubarrays(self, nums, k):
        max_val = max(nums)
        ans = 0
        l = 0
        c = 0
        for num in nums:
            if num == max_val:
                c += 1
            while c >= k:
                if nums[l] == max_val:
                    c -= 1
                l += 1
            ans += l
        return ans
