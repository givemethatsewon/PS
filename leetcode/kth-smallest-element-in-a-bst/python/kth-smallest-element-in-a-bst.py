# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        n = 0 # 현재까지 방문한 노드 수를 파악하기 위한 변수
        # n == k 일때까지 갈거임
        stack = []   # 반복문으로 DFS를 구현하기 위해 스택 활용
        cur = root # 현재 방문중인 노드를 가리키는 포인터

        while cur or stack: # cur이 null이 아니고 stack이 비어있지 않으면 반복
            while cur:
                stack.append(cur) # 왼쪽 자식으로 가기 전 현재 노드 저장
                cur = cur.left  # 가장 왼쪽 노드로 이동

            # 가장 최근에 삽입한 노드를 방문 처리
            cur = stack.pop() 
            n += 1
            if n == k:
                return cur.val
            # if에 걸리지 않았다면
            cur = cur.right # 오른쪽 자식으로 이동 후 다시 반복
