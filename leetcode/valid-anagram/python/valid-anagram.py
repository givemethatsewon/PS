class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): 
            return False
        
        s_chars = [0 for _ in range(26)]
        t_chars = [0 for _ in range(26)]
        
        for c in s:
            s_chars[ord(c) - ord("a")] += 1
        
        for c in t:
            t_chars[ord(c) - ord("a")] += 1
            
        for sc, tc in zip(s_chars, t_chars):
            if sc != tc:
                return False
            
        return True
        
        
        