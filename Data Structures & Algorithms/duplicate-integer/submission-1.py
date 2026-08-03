class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if length of numbers isn't the same as the sorted num(removes duplicates)
        duplicates = len(nums) != len(set(nums)) 
        
        #if there are duplicates
        if duplicates:
            return True
        #if no duplicates
        return False