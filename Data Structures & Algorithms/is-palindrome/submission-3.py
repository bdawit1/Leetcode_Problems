class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 # use the pointer from the left side
        right = len(s) - 1 # start at the right side
        
        while left < right: # while left index is less than right index
            while left < right and not s[left].isalnum(): # while left value isn't a space
                left += 1
            while left < right and not s[right].isalnum(): #while right value isn't a space
                right -=1

            while s[left].lower() != s[right].lower(): #if they aren't the same value,
                return False
            left += 1
            right -= 1
            
        return True #return True if all checks are passed