class Solution(object):
    def containsDuplicate(self, nums):
        num_dict = dict()
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                return True
        return False
        