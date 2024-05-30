class Solution:
    def twoSum(self, nums, target):

        target_table = {}
        for i in range(len(nums)):
            if target - nums[i] not in target_table:
                target_table[nums[i]] = i
            else:
                return [i, target_table[target - nums[i]]]