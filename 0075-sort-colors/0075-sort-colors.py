class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = len([x for x in nums if x == 0])
        b = len([x for x in nums if x == 1])
        c = len([x for x in nums if x == 2])

        nums[:a] = [0] * a  # Replace first a elements with 0
        nums[a:a+b] = [1] * b  # Replace next b elements with 1
        nums[a+b:] = [2] * c 


            