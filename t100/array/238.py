from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_plus = [1] * (n + 1)
        for i in range(0, n):
            left_plus[i+1] = left_plus[i] * nums[i]
        
        right_plus = [1] * (n + 1)
        for i in range(n-1, -1, -1):
            right_plus[i] = right_plus[i+1] * nums[i]
    

        # print(left_plus)
        # print(right_plus)
        left_plus = left_plus[1:]
        right_plus = right_plus[:-1]
        print(left_plus)
        print(right_plus)

        ans = []  
        for i in range(n):
            if i == 0:
                ans.append(right_plus[i+1])
            elif i == n - 1:
                ans.append(left_plus[i-1])
            else:
                ans.append(left_plus[i-1] * right_plus[i+1])
        return ans
    
# 0x3f
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        
        print(pre)
        print(suf)

        return [p * s for p, s in zip(pre, suf)]

# 0x3f
class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        print(suf)

        pre = 1
        for i, x in enumerate(nums):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
            suf[i] *= pre
            pre *= x

        return suf



print(Solution3().productExceptSelf(nums=[1,2,3,4]))
# print(Solution3().productExceptSelf(nums=[-1,1,0,-3,3]))