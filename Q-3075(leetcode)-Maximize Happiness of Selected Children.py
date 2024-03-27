class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness=sorted(happiness,reverse=True)
        sum1=happiness[0]
        k=k-1
        count=0
        i=1
        while k!=0 and i<len(happiness):
            count+=1
            if happiness[i]-count>0:
                sum1+=(happiness[i]-count)
                i+=1
                k-=1
            else:
                break
        return sum1
