class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

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
            
            