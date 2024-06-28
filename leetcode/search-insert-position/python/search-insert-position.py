class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        s , e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            
            if nums[m] < target:
                s = m + 1
            elif target < nums[m]:
                e = m - 1
            else:
                return m
            
        return s