class Solution:

    ##given ["man", "united"]
    ## we need to find the characters in the first words and in the second words
    ## for every words have an integer [4.5]
    ## need to have our integer are the beginning and delimiter (3#man, 6#united)

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs: ## go through every word
            result += str(len(s)) + "#" + s ##add word length, delimited, and word
        return result  

    def decode(self, s: str) -> List[str]:
        result = [] #list of words
        i = 0 

        while i < len(s): # while the entire string 
            j = i # use j to find the delimiter
            while s[j] != "#": # while we dont have the delimtied
                j += 1 # increment by 1
            length = int(s[i:j]) #digits from i to delimiter (#)
            #s[j + 1: j + 1 + length] # first character after delimiter (#) to end of the string            
            result.append(s[j + 1: j + 1 + length]) # grab that many chars AFTER the "#": the word
            i = j + 1 + length # set i to the beginning of the next string
        return result

