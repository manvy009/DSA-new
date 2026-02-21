class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        total_weight = sum(weights)
    
        low, high = max_weight, total_weight
        while low <= high:
            mid = (low + high) // 2
            current_load = 0
            required_days = 1
            for weight in weights:
                if current_load + weight > mid:
                    required_days += 1
                    current_load = 0
                current_load += weight
            if required_days <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low