from typing import List

# 0x3f
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            if nums[i] + nums[-1] + nums[-2] < 0:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return ans
