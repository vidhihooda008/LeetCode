class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path, remaining):
            # Base case: if no numbers left, add path
            if not remaining:
                res.append(path)
                return
            
            # Try each number in remaining
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return res
