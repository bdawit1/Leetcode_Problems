class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #division between two integers round to 0.  
        ## 2,1,+,3, * 
        ## (2 + 1) * 3 = 3 * 3 = 9

        stack = []

        for char in tokens:
            ## if the char is "+" 
            if char == "+":
                ##  append the two added values of the stack
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                ## order matters (a is first pop, b is second pop)
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
                #stack append second - first
            elif char == "*":
                ##  append the two added values of the stack
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                ## order matters (a is first pop, b is second pop)
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
                #stack appened second / first (using int rounds to 0)
            else:
                stack.append(int(char))
                #if it is a number continue 
        return stack[0]
        #return the only value left in the stack