class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        import math
        
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(pile / float(mid)) for pile in piles)
            
            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

        