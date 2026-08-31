class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ##need to figure out how to elimnate duplicate values 
        ## [2,3,6,7]    Target = 7
        ## all combinations of 6 are greater than 7
        ## make a DFS decision tree with no repeats 
        # DFS parameters:
        # - index: forces us to move left-to-right so we don't end up with duplicate
        #          combos like [2, 3] and [3, 2].
        # - curr: our working list of picked numbers.
        # - totalSum: keeps score in real-time so we don't waste time running sum(curr)
        #             at every single step.
        result = []
        def DFS(index, curr, totalSum):

            # WE FOUND A MATCH!
            if totalSum == target:
                # Store curr[:] (a snapshot copy). If we stored 'curr' directly,
                # Python's pass-by-reference means future pops would empty it out.
                result.append(curr[:])
                return

            # DEAD END: run out of numbers or went over the target. Stop exploring.
            if index >= len(nums) or totalSum > target:
                return

            # OPTION 1: "Let's try picking this number."
            curr.append(nums[index])
            # Stay on the SAME index so we can reuse this number again if we want.
            DFS(index, curr, totalSum + nums[index])

            # BACKTRACK: "Take it back out" to clean up 'curr' before trying Option 2.
            curr.pop()

            # OPTION 2: "Skip this number completely and move to the next one."
            # totalSum stays the same because we didn't add anything to 'curr'.
            DFS(index + 1, curr, totalSum)

        # Start exploring from the very first element with a sum of 0
        DFS(0, [], 0)
        return result