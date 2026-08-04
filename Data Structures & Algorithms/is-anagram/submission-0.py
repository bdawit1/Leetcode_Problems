class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        found_s = {}                            # dictionary of each character in s
        found_t = {}                            # dictionary of each character in t

        for char in s:                          # go through every character in s
            found_s[char] = found_s.get(char, 0) + 1   # add 1 to this char's count if its new
        for char in t:                          # go through every character in t
            found_t[char] = found_t.get(char, 0) + 1   # add 1 to this char's count if its new

        return found_s == found_t               # f they contain the same characters, return true, else return false