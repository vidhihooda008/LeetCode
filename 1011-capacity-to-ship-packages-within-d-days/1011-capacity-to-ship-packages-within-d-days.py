class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # Helper function to check if a given capacity works
        def canShip(capacity):
            d = 1
            current = 0
            for w in weights:
                if current + w > capacity:
                    d += 1
                    current = 0
                current += w
            return d <= days

        # Binary search range
        left, right = max(weights), sum(weights)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
