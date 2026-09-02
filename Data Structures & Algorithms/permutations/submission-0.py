class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## need to get all combinations/ permuations of nums list.
        
        if len(nums) == 0:
            return [[]]
            # if there are no numbers in num return nothing 
        
        perms = self.permute(nums[1:])         # start perfmutation after the first number

        result = [] # result for the perms
        for p in perms:
            for i in range(len(p) + 1): ## go through every possible index (can add to the end of permutation so do a + 1)
                
                p_copy = p.copy() # create a copy because you can add multiple vlaues
                p_copy.insert(i, nums[0]) #takes the first number of the array (nums[0]) and inserts it into position i of the existing permutation copy (p_copy).
                result.append(p_copy) ## append this to the results
        return result


