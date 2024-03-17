class Solution:
    def insert(self, nums: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(nums)
        res= []
        while i < len(nums):
            if nums[i][1]<newInterval [0]:
                res.append(nums[i])
            elif nums[i][0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(newInterval[0], nums[i][0])
                newInterval[1] = max(newInterval[1], nums[i][1])
            i += 1
        res.append(newInterval)
        while i < n:
            res.append(nums[i])
            i += 1
        return res
