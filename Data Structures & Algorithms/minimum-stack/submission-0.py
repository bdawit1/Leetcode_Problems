class MinStack:
    # want to get the top value on the stack
    # and want to be able to retrieve the minimum element in constant time 
    ## HINT: consider each node in the stack to have a corresponding minimum value. 
    ## dont replace the minimum unless it actually is less than the min. if its the same doesn't matter
    ## make sure the minimum is stored so when it gets popped it still is the same     until you reach a new minimum
    ## when you do getMin, you just look at the stack that only stores the minimum
    def __init__(self):
        ##need two stacks (stack and min_stack)
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #need to know if there already a val in the min stack, need to check the val of the top of the min.stack
        val = min(val, self.minStack[-1] if self.minStack else val) ##the if statement means if the stack is non empty
        self.minStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    #r# return top of stack
    def top(self) -> int:
        return self.stack[-1]

    ## return top of minStack
    def getMin(self) -> int:
        return self.minStack[-1]
