class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 
        right = len(numbers) - 1

        #while the pointers don't overlap
        while left < right:
            #current sum is the numbers of the value of the left pointer + the right pointer
            currentSum = numbers[left] + numbers[right]
            #if the target is less than needed move the numbers left value down one position
            if currentSum < target:
                left += 1
            #if the target is greater than needed move the numbers right value down one position
            elif currentSum > target:
                right -= 1
            #add +1 because of zero indexing.
            else:
                return [left + 1, right + 1]
        return []