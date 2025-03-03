from typing import List

class Solution:
    """
    55. Jump Game
    Given an array of non-negative integers nums, 
    you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length.
    
    Return True if you can reach the last index, otherwise return False.
    
    Example:
    Input: nums = [2,3,1,1,4]
    Output: True
    
    Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^5
    """

    def canJump(self, nums: List[int]) -> bool:
        right = 0
        length = len(nums) - 1
        for i in range(len(nums)):
            if i > right:
                return False
            right = max(right, nums[i] + i)
            if right >= length:
                return True
        return False
