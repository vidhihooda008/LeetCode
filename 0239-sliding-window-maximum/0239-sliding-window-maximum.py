from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()  # stores indices
        result = []
        
        for i in range(len(nums)):
            # Step 1: Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Step 2: Add current index
            dq.append(i)
            
            # Step 3: Remove out-of-window index from front
            if dq[0] <= i - k:
                dq.popleft()
            
            # Step 4: Record max once window is full
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
