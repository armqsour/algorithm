from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        left = right = 0

        while right < len(nums) - 1:
            if nums[right + 1] != 0 and nums[left] == 0:
                nums[left], nums[right + 1] = nums[right + 1], nums[left]
                left += 1
                right += 1
            elif nums[right + 1] == 0 and nums[left] != 0:
                left += 1
                right += 1
            elif nums[left] != 0 and nums[right + 1] != 0:
                left += 1
                right += 1
            else:
                right += 1

# 0x3f
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        stack_size = 0
        for x in nums:
            if x:
                nums[stack_size] = x  # 把 x 入栈
                stack_size += 1
        for i in range(stack_size, len(nums)):
            nums[i] = 0