class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        stk=[]
        for i,j in d.items():
            stk.append(j)
        x=max(stk)
        sum1=0
        for i in stk:
            if i==x:
                sum1+=i
        return sum1
