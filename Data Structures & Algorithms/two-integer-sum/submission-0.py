class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        position = {}

        for i,n in enumerate(nums):
            if target - n in position:
                return [position[target - n], i]
            position[n] = i
        return []