class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ### nums [1,2,3,4] Let's use 3
        ### prefix  [1,2,6,24] # multiply every number before 3
        ### postfix [24,24,12,4] #every number after 3
        ### for position 1: 1 * 24 = 24 because 2 * 3 * 4 = 24
        ### for position 2: 1 * 12 = 12 because 1 * 3 * 4 = 12
        ### for position 3: 2 *  4 = 8  because 1 * 2 * 4 = 8
        ### for position 4: 6 *  1 = 6  becuase 1 * 2 * 3 = 6
        ### output [24,12,8,6]
        
        result = [1] * len(nums) #start at 1 * len of array

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix # for each position in our prefix array we put it in i
            prefix = prefix * nums[i] # take input array val (num[i]) by prefix
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #range of end of array to beginning
            result[i] = result[i] * postfix #value in result * postfix
            postfix = postfix * nums[i] #update postfix to value in input array(nums)
        return result
            
            
