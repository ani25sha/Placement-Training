class Solution:
    def maximumProduct(self, numbers: List[int]) -> int:
        numbers.sort()
        return max(numbers[-1] * numbers[-2] * numbers[-3], numbers[0] * numbers[1] * numbers[-1])