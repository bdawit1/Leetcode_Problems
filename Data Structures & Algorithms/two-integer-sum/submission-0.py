class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}                          # keeps track of numbers I've seen and where they were

        for i, n in enumerate(nums):           # go through the list, i is the index, n is the number
            if target - n in position:         # check if the number I need to hit the target is already saved
                return [position[target - n], i]   # found it, send back both indices
            position[n] = i                    # not found yet, so save this number and its index for later
        return []                              # got through the whole list with no pair

        # Time:  O(n)  - walk through the list once, and each dictionary
        #               lookup/insert is O(1) on average, so n items = n work
        # Space: O(n)  - in the worst case we store almost every number in the
        #               dictionary before finding a pair, so memory grows with n
