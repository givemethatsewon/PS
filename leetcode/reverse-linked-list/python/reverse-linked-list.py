# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # head를 타고 이동하면서 뒤집자.
        curr = head
        temp = None

        while curr != None:
            next_node = curr.next # 다음 노드 정보 미리 저장
            curr.next = temp
            temp = curr # 현재 노드로 업데이트
            curr = next_node # 다음 노드로 이동
            
        return temp