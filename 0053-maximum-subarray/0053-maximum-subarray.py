import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -sys.maxsize-1 # maximum sum
        sum = 0
        n = len(nums)
        for i in range(n):
            sum += nums[i]

            if sum > maxi:
                maxi = sum

            # If sum < 0: discard the sum calculated
            if sum < 0:
                sum = 0

        # To consider the sum of the empty subarray
        # uncomment the following check:

        #if maxi < 0: maxi = 0

        return maxi
