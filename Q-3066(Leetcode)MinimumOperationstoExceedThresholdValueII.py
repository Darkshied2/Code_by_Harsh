class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) 
        counter = 0
        while len(nums)>1 and nums[0]<k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            heapq.heappush(nums, 2*a+b)
            counter += 1
        return counter
