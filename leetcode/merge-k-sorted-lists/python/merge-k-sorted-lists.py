# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1: 
            mergedLists = []

            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge(left, right)) 
            lists = mergedLists
        return lists[0]

    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right 

        return dummy.next
