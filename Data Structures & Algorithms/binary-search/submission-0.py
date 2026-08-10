class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 #left pointer
        high = len(nums)-1 #right pointer

        while low <= high:
            mid = (low + high) // 2 ##middle point
            if nums[mid] == target: # if the middle index is at the target
                return mid #return the index
            elif nums[mid] < target: #if we havent reached the target
                low = mid + 1 #increase the mid by 1
            else: 
                high = mid - 1 #decrease the mid by 1
        
        return -1 ## return -1 if there isn't a target point