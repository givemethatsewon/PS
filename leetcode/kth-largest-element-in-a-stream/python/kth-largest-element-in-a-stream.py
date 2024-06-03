class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.sorted_nums = sorted(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        nums = self.sorted_nums

        start, end = 0, len(nums) - 1
        mid = None
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < val:
                start = mid + 1
            else:
                end = mid - 1

        nums.insert(start, val)

        return nums[-self.k]