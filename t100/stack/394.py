from io import StringIO
from itertools import count


class Solution:
    def decodeString(self, s: str) -> str:
            stack = []
            curr_str = ""
            curr_num = 0

            for c in s:
                if c.isdigit():
                    # 处理多位数，如 "12" -> 1*10 + 2 = 12
                    curr_num = curr_num * 10 + int(c)
                elif c == '[':
                    # 遇到左括号，把当前的字符串和倍数压入栈，开始处理括号内的新字符串
                    stack.append((curr_str, curr_num))
                    curr_str = "" # 重置，准备收集括号内的字符
                    curr_num = 0  # 重置，准备收集嵌套内部的数字
                elif c == ']':
                    # 遇到右括号，弹出栈顶的 (上层字符串, 重复次数)
                    last_str, num = stack.pop()
                    # 核心逻辑：上层字符串 + (当前字符串 * 重复次数)
                    curr_str = last_str + num * curr_str
                else:
                    # 普通字母
                    curr_str += c

            return curr_str

# 0x3f
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s

        # s[0] 是字母
        if s[0].isalpha():
            # 分离出 s[0]，解码剩下的
            return s[0] + self.decodeString(s[1:])

        # s[0] 是数字，后面至少有一对括号
        i = s.find('[')  # 找左括号
        # 找右括号，注意对于 [...[...]...] 这种情况，第一个右括号并不是我们要找的，第二个才是
        balance = 1  # 左括号个数减去右括号个数
        for j in count(i + 1):  # 从 i+1 开始向右遍历，找与 s[i] 匹配的右括号
            if s[j] == '[':
                balance += 1
            elif s[j] == ']':
                balance -= 1
                if balance == 0:  # 左右括号个数相等，找到与 s[i] 匹配的右括号 s[j]
                    return self.decodeString(s[i + 1: j]) * int(s[:i]) + self.decodeString(s[j + 1:])

# 0x3f
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def decode() -> str:
            nonlocal i
            res = ''  # 或者 res = []，具体见另一份代码【Python3 列表】
            k = 0
            while i < len(s):
                c = s[i]
                i += 1
                if c.isalpha():
                    res += c
                elif c.isdigit():
                    k = k * 10 + int(c)
                elif c == '[':  # 递
                    res += decode() * k  # 把括号内的字符串重复 k 次
                    k = 0  # 重置 k，若不重置，2[a]3[b] 后面的 3 会算出 k = 23
                else:  # ']' 归
                    break
            return res

        return decode()

print(Solution().decodeString("3[a2[c]]"))