class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_nums = set(nums)        ##sort the numbers in order
        longest_streak = 0 


        for num in ordered_nums: ##if the number is in the ordered_nums set
            if num - 1 not in ordered_nums: ## if the array only has one number
                current_num = num ##set the number to a new current number
                current_streak = 1 ## make the streak 1

                while current_num + 1 in ordered_nums: ##if the current number is a sequence to the next number
                    current_num += 1 #increment the current number by 1
                    current_streak += 1 # increase streak

                if current_streak > longest_streak: 
                    longest_streak = current_streak 
        return longest_streak
        
## NEED LAST IF STATEMENT BECAUSE:
#return current_streak at the very end of the code, it will just spit out the score of the last sequence it looked at before the loop finished, because previous sequences were erased.
        