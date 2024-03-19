class Solution:
    def productExceptSelf(self, nums, n):
        res=[1]*n
        prefix=1
        for i in range(len(res)):
            res[i] *= prefix
            prefix*=nums[i]
        postfix=1
        
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix *= nums[i]
            
        return res