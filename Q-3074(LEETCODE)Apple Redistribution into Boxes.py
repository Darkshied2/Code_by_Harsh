class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        t=sum(apple)
        i = 0
        while t>0 and i<len(capacity):
            t-=capacity[i]
            i+=1
        return i
            
        
