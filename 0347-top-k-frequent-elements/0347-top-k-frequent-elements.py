import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)  # count frequencies
        # Use heapq.nlargest to get k elements by frequency
        return heapq.nlargest(k, freq.keys(), key=freq.get)

        