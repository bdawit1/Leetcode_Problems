class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] ## stores the final list of all subsets

        def backtrack(index, path): 
            # base case for all elements in nums
            if index == len(nums):
                result.append(path[:]) #append a copy of path
                return 

            #choice 1: include nums[index] in subset
            path.append(nums[index]) ##add elemnts to path 
            backtrack(index + 1, path) #recursively go to the next element
            path.pop() #remove nums[index] to test it 

            #choice 2: exclude nums[index]
            backtrack(index + 1, path) # #recursively go to the next element

        backtrack(0, [])#start recursion at 0 with an emoty path "backtrack(index,path)"
        return result #return new list of all subsets.