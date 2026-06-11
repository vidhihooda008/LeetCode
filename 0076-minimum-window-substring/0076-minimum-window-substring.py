from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            
            # When all chars are included
            if missing == 0:
                # Shrink from left
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # Update best window
                if end == 0 or right - left < end - start:
                    start, end = left, right
                
                # Prepare for next window
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]
