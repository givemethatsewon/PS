class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        left = lists.pop()
        right = lists.pop()
        
        merged = self.merge(left, right)
        lists.append(merged)
        
        return self.mergeKLists(lists)
            
    
    def merge(self, left, right):
        dummy = ListNode(0)
        current = dummy
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
                            
            current = current.next
        
        if left:
            current.next = left
        if right:
            current.next = right
        
        return dummy.next