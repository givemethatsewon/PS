class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        word = str(x)
        for i in range(len(word) // 2):
            j = len(word) - 1 - i
            if word[i] != word[j]:
                return False
        return True
        

        