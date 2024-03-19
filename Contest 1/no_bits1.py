class Solution:
    def hammingWeight(self, num: int) -> int:
        # Initialize a variable to store the count of set bits
        set_bits_count = 0
        
        # Iterate until num becomes zero
        while num:
            # Increment the count if the rightmost bit is set (equals 1)
            set_bits_count += num % 2
            
            # Right shift num by one position to discard the rightmost bit
            num >>= 1
        
        # Return the count of set bits
        return set_bits_count