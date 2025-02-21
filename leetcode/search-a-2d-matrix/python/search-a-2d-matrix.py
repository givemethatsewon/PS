class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            line = matrix[i]
            left, right = 0, n-1

            while left <= right:
                # mid 계산
                mid = (left + right) // 2
                # target이 더 클때
                if target > line[mid]:
                    left = mid + 1
                # target이 더 작을 때
                elif target < line[mid]:
                    right = mid - 1
                # 같을 때
                else:
                    return True
        
        return False


        