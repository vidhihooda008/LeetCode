class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        
        def canPlaceBalls(force):
            count = 1  # place first ball
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= force:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans

        