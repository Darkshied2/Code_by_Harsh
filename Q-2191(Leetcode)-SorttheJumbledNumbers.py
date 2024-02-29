class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        data={}
        ans=[]
        for i in range(len(nums)):
            val = ''
            for j in str(nums[i]):
                val += str(mapping[int(j)])
            if int(val) in data:
                data[int(val)].append(nums[i])
            else:
                data[int(val)] = [nums[i]]
        for k in sorted(data.keys()):
            ans += data[k]
        return ans
