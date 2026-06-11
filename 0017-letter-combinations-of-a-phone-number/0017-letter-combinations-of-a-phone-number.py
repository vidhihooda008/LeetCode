class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, path):
            # Base case: if we've used all digits
            if index == len(digits):
                res.append(path)
                return
            
            # Explore all possible letters for current digit
            for char in phone_map[digits[index]]:
                backtrack(index + 1, path + char)
        
        backtrack(0, "")
        return res

        