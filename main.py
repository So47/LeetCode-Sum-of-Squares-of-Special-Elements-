class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            # Adjust for 1-indexing by checking if n % (i+1) == 0
            if n % (i+1) == 0: 
                result += nums[i] * nums[i]
        return result        
