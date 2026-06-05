class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        
        return countS == countT
