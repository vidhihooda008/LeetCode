class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        
        # Step 1: Count frequencies
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        # Step 2: Find first non-repeating character
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        
        return -1
