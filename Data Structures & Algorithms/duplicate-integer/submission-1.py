class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate=[]
        def d(nums):
        
            for i in range(len(nums)):
                if nums[i] not in duplicate:
                    duplicate.append(nums[i])
                else:
                    return True
            return False
        return d(nums)
