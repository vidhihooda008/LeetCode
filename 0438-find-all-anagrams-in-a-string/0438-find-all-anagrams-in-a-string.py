from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        len_p = len(p)
        count_p = Counter(p)
        count_s = Counter()
        
        for i, ch in enumerate(s):
            # Add current char to window
            count_s[ch] += 1
            
            # Remove char left of window
            if i >= len_p:
                left_char = s[i - len_p]
                count_s[left_char] -= 1
                if count_s[left_char] == 0:
                    del count_s[left_char]
            
            # Compare window with target
            if count_s == count_p:
                res.append(i - len_p + 1)
        
        return res
