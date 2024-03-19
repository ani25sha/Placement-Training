import math

class Solution:
    def minSubArrayLen(self, target: int, numbers: List[int]) -> int:
        start, end, current_sum = 0, 0, 0
        min_length = math.inf
        n = len(numbers)
        for end in range(n):
            current_sum += numbers[end]
            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= numbers[start]
                start += 1
        return min_length if min_length != math.inf else 0