class Solution:
    def isValid(self, s: str) -> bool:
        
    ##Open Brackets Must be closed by the same type of brackets.
    ##Open Bracks must be closes in the correct order.
    ## {}, (), []

        stack = []
        # Map each closing bracket to its corresponding opening bracket
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in closeToOpen:
                # If it's a closing bracket, check for a matching opening bracket on top of the stack
                if stack and stack[-1] == closeToOpen[i]: 
                    stack.pop()
                else:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(i)

        return not stack