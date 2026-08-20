class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        p=1
        for j in range(len(nums)):
            res[j]=p
            p=p*nums[j]
      
        s=1
        j=len(nums)-1
        while j >=0:
            res[j]*=s
            s=s*nums[j]
            j-=1
        return res
        # return s(nums)