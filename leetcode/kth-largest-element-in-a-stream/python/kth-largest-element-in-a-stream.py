class KthLargest(object):

    def __init__(self, k, nums):
        # min heap with k largest elements
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)     # O(n)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        # edge case
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)     # return min value
        return self.minHeap[0]