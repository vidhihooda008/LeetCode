class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(curr, open_count, close_count):
            # Base case: if the string is complete
            if len(curr) == 2 * n:
                res.append(curr)
                return
            
            # Add "(" if we still have opens left
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            
            # Add ")" if we have more opens than closes
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res
