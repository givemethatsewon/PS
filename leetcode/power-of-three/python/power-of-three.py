class Solution(object):
    def isPowerOfThree(self, n):
        flag = True

        if n <= 0:
            return False
        elif n == 1:
            return True
        
        while n >= 2:
            if n % 3 != 0:
                flag = False
                break
            n = n // 3
        
        return flag
        