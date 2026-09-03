class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## there are numbers when they aren't greater than the number before hand 
        ## return a default value of 0
        ## have to store all of the previous temperautes, cannot override them
        ## using a stack to store all the previous temperatures
        ## will use stack.pop() when a bigger number is found. 
        ## need to do monotonic decreasing stack problem 

        result = [0] * len(temperatures) ##start at default values of zero with temperatue length
        stack = [] # pair of [temp,index] 

        for i,t in enumerate(temperatures): #get index and value at the same time
            while stack and t > stack[-1][0]: #if stack is empty and is it greater than value at the top of the stack.
                stackTemperature, stackIndex = stack.pop() #pop both the temperature and the index
                result[stackIndex] = (i - stackIndex) #for result, now we want to find how many days it took to find the greater temperature from our current index
            stack.append([t,i]) ## append the temperature and the index to the stack
        return result