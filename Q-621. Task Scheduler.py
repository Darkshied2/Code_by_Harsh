class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())
        maxCount = 0

        for key,val in count.items():
            if val==maxFreq:
                maxCount+=1

        space = (maxFreq-1)*max(0,n-maxCount+1)
        remTaskCount = max(0,len(tasks)-(maxFreq*maxCount)-space)

        return maxFreq*maxCount+space+remTaskCount
