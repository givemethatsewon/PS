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
        self.sorted_nums.append(val)
        self.sorted_nums.sort()
        return self.sorted_nums[-self.k]









# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)