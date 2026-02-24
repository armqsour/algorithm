class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return len(s)
        ans = 0
        tmp_set = set()
        for i in range(n):
            k = i
            while k < n:
                if s[k] not in tmp_set:
                    tmp_set.add(s[k])
                    k += 1
                else:
                    ans = max(ans, len(tmp_set))
                    tmp_set.clear()
                    break
        return ans

# 0x3f
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        window = set()  # 维护从下标 left 到下标 right 的字符
        for right, c in enumerate(s):
            # 如果窗口内已经包含 c，那么再加入一个 c 会导致窗口内有重复元素
            # 所以要在加入 c 之前，先移出窗口内的 c
            while c in window:  # 窗口内有 c
                window.remove(s[left])
                left += 1  # 缩小窗口
            window.add(c)  # 加入 c
            ans = max(ans, right - left + 1)  # 更新窗口长度最大值
        return ans
