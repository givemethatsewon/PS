class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums) - 1
        res = min(nums[low], nums[high])

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > res:
                low = mid + 1
            else:
                res = min(nums[mid], res)
                high = mid - 1
        
        return res
        