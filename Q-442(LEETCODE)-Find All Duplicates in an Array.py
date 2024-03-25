class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=[]
        nums=Counter(nums)
        for i,j in nums.items():
            if (j==2):
                s.append(i)a
        return s
