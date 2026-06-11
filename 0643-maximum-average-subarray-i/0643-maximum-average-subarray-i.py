class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Step 1: Compute sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Step 2: Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        # Step 3: Return maximum average
        return float(max_sum) / k
