class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def iscap(cap):
            day_count = 1
            curr_load = 0
            for w in weights:
                if curr_load + w > cap:
                    day_count += 1
                    curr_load = w
                    if day_count > days:
                        return False
                else:
                    curr_load += w
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if iscap(mid):
                right = mid
            else:
                left = mid + 1
        return left
        