class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       ###group them into smaller subslist
       ##if you swap tan and nat they are equivalent strings
       ## two strings are anargrams of each other if they cant be sorted.

       #count[a-z] one letter for each word
       ## Time O(m * n)

        result = defaultdict(list) # hashmap of character Count to the list of anagrams

        for i in strs:
            count = [0] * 26 # a - z
        
            for char in i: #for the characters in i 
                count[ord(char) - ord("a")] += 1 #ascii value of i - ascii "a"
        
            result[tuple(count)].append(i) #    # tuple() because lists can't be dict keys, tuples can
        
        return list(result.values()) 

         