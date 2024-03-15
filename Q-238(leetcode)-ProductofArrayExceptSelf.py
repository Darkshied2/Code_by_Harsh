class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = len(nums)*[1]   
        pre = len(nums)*[1]    
        post= len(nums)*[1]    
        pref, postf = 1 , 1     
        for i in range(len(nums)):
            pre[i]= pref       
            pref *= nums[i]    
        for i in range(len(nums)-1,-1,-1):
            post[i]= postf      
            postf *=nums[i]    
        result[0]= post[0]
        result[len(nums)-1] = pre[len(nums)-1]  
        for i in range (1,len(nums)-1):
            result[i]=pre[i]*post[i]  
        return result
