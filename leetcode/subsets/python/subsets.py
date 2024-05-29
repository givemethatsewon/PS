class Solution(object):
    def subsets(self, nums):
        def backtrack(start, path):
            # 현재 경로를 결과에 추가
            result.append(path)
            
            # 가능한 모든 다음 요소들을 탐색
            for i in range(start, len(nums)):
                # 현재 요소를 포함하여 다음 재귀 호출을 수행
                backtrack(i + 1, path + [nums[i]])
        
        result = []
        backtrack(0, [])
        return result
        
        